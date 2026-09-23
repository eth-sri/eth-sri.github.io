# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "fire",
#     "mip==1.16rc0",
#     "cffi==2.0.0.b1",
#     "edit_distance==1.0.9",
# ]
# ///
import random
import csv
from datetime import datetime
import sys
import fire
import edit_distance
random.seed(0)

FIXED_ASSIGNMENT = {
    "Computer science achievement and writing skills predict vibe coding proficiency": "Dario Llarden",
    "Validating JVM Compilers via Maximizing Optimization Interactions": "Malte Dömer",
}
def row_of_student_name(
    student_name: str,
    enrollment: list[list[str]],
):
    min_dist = float("inf")
    student = None
    for row in enrollment:
        student_name_official = f"{row[2]} {row[0]}"
        dist_matcher = edit_distance.SequenceMatcher(a=student_name, b=student_name_official)
        dist = dist_matcher.distance()
        if dist < min_dist:
            min_dist = dist
            student = row
    return student


def solve_assignment_milp(
    paper_names: list[str],
    students: list[str],
    student_preferences: dict[str, list[str]],
):
    """
    Minimize total sum of assigned rankings, i.e. sum of ranks of assigned papers for each student.
    """
    n_students = len(students)
    m_papers = len(paper_names)
    student_preferences: dict[int, list[int]] = {
        students.index(student): [paper_names.index(p) for p in prefs]
        for student, prefs in student_preferences.items()
    }
    from mip import Model, xsum, minimize, BINARY
    model = Model("MILP_01")
    model.verbose = 0
    copied_pref_dict = {}
    for student in range(n_students):
        copied_pref_dict[student] = [model.add_var(var_type=BINARY) for _ in range(m_papers)]
    # Change to minimization problem.
    model.objective = minimize(
        xsum(
            copied_pref_dict[student][paper] * (i + 1)**10
            for student, prefs in student_preferences.items()
            for i, paper in enumerate(prefs)
        )
    )
    # enforce that each student is assigned to exactly one paper
    for student in range(n_students):
        model += xsum(copied_pref_dict[student]) == 1
    # enforce that each paper is assigned to at most one student
    for paper in range(m_papers):
        model += xsum(copied_pref_dict[student][paper] for student in range(n_students)) <= 1
    model.optimize()
    # generate the assignment
    paper_assigned = {
        paper: None for paper in paper_names
    }
    for student, prefs in student_preferences.items():
        for i, paper in enumerate(prefs):
            if copied_pref_dict[student][paper].x >= 0.9:
                paper_assigned[paper_names[paper]] = students[student]
    return paper_assigned


def assign_papers(
    paper_file_path: str,
    student_enrolment_file_path: str,
    student_preferences_file_path: str,
):
    # Read the CSV file of papers
    filename = paper_file_path
    paper_rows = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if any(row[0].startswith(s) for s in ("Lab", "By Lab", "Dates")) or not row[0]:
                # skip headers
                continue
            paper_rows.append(row)

    # Read the tabbed content of the student enrollment
    filename = student_enrolment_file_path
    enrollment = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            enrollment.append(tuple(x.strip() for x in row))
    # get the enrolled legi numbers (col 4)
    enrolled_legis = set(e[3].replace("-", "") for e in enrollment)

    # Read the CSV file of student preferences
    filename = student_preferences_file_path
    student_rows = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if any(row[0].startswith(s) for s in ("Timestamp")) or not row[0]:
                # skip headers
                continue
            # check that the student is enrolled
            if row[3].replace("-", "") not in enrolled_legis:
                continue
            student_rows.append(tuple(x.strip() for x in row))
    
    # extract the latest submission for each student
    students = set(s[3] for s in student_rows)
    submissions = {}
    for row in student_rows:
        submissions[row[3]] = row


    paper_names = [p[1] for p in paper_rows if p[1] not in FIXED_ASSIGNMENT]
    students = list(students)
    student_preferences = {}
    for student, sub in submissions.items():
        prefs = []
        for i in range(4, 11):
            if sub[i] in paper_names:
                prefs.append(sub[i])
        non_submitted_prefs = [p for p in paper_names if p not in prefs]
        random.shuffle(non_submitted_prefs)
        prefs += non_submitted_prefs
        student_preferences[student] = prefs

    paper_assigned = solve_assignment_milp(
        paper_names=paper_names,
        students=students,
        student_preferences=student_preferences
    )

    paper_by_name = {p[1]: p for p in paper_rows}
    student_by_legi = {s[3]: s for s in student_rows}
    writer = csv.writer(sys.stdout)
    writer.writerow(["Name", "Email", "Legi", "Ranked position", "Lab", "Paper title", "Paper link", "..."])
    student_belegung_by_legi = {s[3]: s for s in enrollment}
    for paper in paper_rows:
        paper_name = paper[1]
        if paper_name in FIXED_ASSIGNMENT:
            student_belegung_row = row_of_student_name(FIXED_ASSIGNMENT[paper_name], enrollment)
            student_comments = ("Fixed as first lecture",)
            is_among_preferences = True
        elif paper_assigned[paper_name] is None:
            continue
        else:
            legi = paper_assigned[paper_name]
            student_details = student_by_legi[legi]
            student_details = tuple(x.replace("\n", r"\n") for x in student_details)
            student_comments = student_details[11:]
            is_among_preferences = student_preferences[student_details[3]].index(paper_name)
            student_belegung_row = student_belegung_by_legi[legi]
        student_details = (
            f"{student_belegung_row[2]} {student_belegung_row[0]}",
            student_belegung_row[15],
            student_belegung_row[3],
        )
        writer.writerow(student_details + (is_among_preferences,) + tuple(paper_by_name[paper_name]) + student_comments)

if __name__ == "__main__":
    fire.Fire(assign_papers)
