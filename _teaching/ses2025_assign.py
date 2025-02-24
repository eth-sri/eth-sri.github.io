import random
import csv
from datetime import datetime
import sys
import fire
random.seed(0)

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
    copied_pref_dict = {}
    for student in range(n_students):
        copied_pref_dict[student] = [model.add_var(var_type=BINARY) for _ in range(m_papers)]
    # Change to minimization problem.
    model.objective = minimize(
        xsum(
            copied_pref_dict[student][paper] * (i + 1)
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

def simple_assignment(
    paper_names: list[str],
    students: list[str],
    student_preferences: dict[str, list[str]],
):
    # assignment algorithm: stable marriage where students are randomized, non submitted preferences are randomized
    paper_assigned = {
        p: None for p in paper_names
    }
    students = list(students)
    random.shuffle(students)
    students_assigned = set()
    for i in range(len(paper_assigned)):
        for student in students:
            if student not in students_assigned:
                preferred_paper = student_preferences[student][i]
                if not paper_assigned.get(preferred_paper):
                    paper_assigned[preferred_paper] = student
                    students_assigned.add(student)
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
            if any(row[0].startswith(s) for s in ("Lab", "By Lab")) or not row[0]:
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


    paper_names = [p[1] for p in paper_rows]
    students = list(students)
    student_preferences = {}
    for student, sub in submissions.items():
        prefs = []
        for i in range(4, 11):
            if sub[i]:
                prefs.append(sub[i])
        non_submitted_prefs = [p for p in paper_names if p not in prefs]
        random.shuffle(non_submitted_prefs)
        prefs += non_submitted_prefs
        student_preferences[student] = prefs

    # paper_assigned = simple_assignment(
    #     paper_names=paper_names,
    #     students=students,
    #     student_preferences=student_preferences
    # )
    paper_assigned = solve_assignment_milp(
        paper_names=paper_names,
        students=students,
        student_preferences=student_preferences
    )


    paper_by_name = {p[1]: p for p in paper_rows}
    student_by_legi = {s[3]: s for s in student_rows}
    writer = csv.writer(sys.stdout)
    writer.writerow(["Name", "Email", "Legi", "Ranked position", "Lab", "Paper title", "Paper link", "..."])
    for paper in paper_rows:
        paper_name = paper[1]
        if paper_assigned[paper_name] is None:
            continue
        student_details = student_by_legi[paper_assigned[paper_name]]
        student_details = tuple(x.replace("\n", r"\n") for x in student_details)
        is_among_preferences = student_preferences[student_details[3]].index(paper_name)
        writer.writerow(student_details[1:4] + (is_among_preferences,) + tuple(paper_by_name[paper_name]) + student_details[11:13])

if __name__ == "__main__":
    fire.Fire(assign_papers)