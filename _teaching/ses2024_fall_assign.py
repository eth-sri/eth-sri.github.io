import random
import csv
from datetime import datetime
import sys
random.seed(0)

# Read the CSV file of papers
filename = sys.argv[1]
paper_rows = []
with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if any(row[0].startswith(s) for s in ("SRI", "AST", "Paper title")) or not row[0]:
            # skip headers
            continue
        paper_rows.append(tuple(x.strip() for x in row))

# Read the tabbed content of the student enrollment
filename = sys.argv[3]
enrollment = []
with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    for row in reader:
        enrollment.append(tuple(x.strip() for x in row))
# get the enrolled legi numbers (col 4)
enrolled_legis = set(e[3].replace("-", "") for e in enrollment)

# Read the CSV file of student preferences
filename = sys.argv[2]
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
students = set(s[2] for s in student_rows)
submissions = {}
for row in student_rows:
    submissions[row[2]] = row


# assignment algorithm: stable marriage where students are randomized, non submitted preferences are randomized
paper_assigned = {
    p[0]: None for p in paper_rows
}
students_assigned = set()
students = list(students)
random.shuffle(students)
student_preferences = {}
for student, sub in submissions.items():
    prefs = [
        sub[4],
        sub[5],
        sub[6],
    ] + ([sub[7]] if sub[7] else []) + ([sub[8]] if sub[8] else [])
    non_submitted_prefs = [p for p in paper_assigned if p not in prefs]
    random.shuffle(non_submitted_prefs)
    prefs += non_submitted_prefs
    student_preferences[student] = prefs

for i in range(len(paper_assigned)):
    for student in students:
        if student not in students_assigned:
            preferred_paper = student_preferences[student][i]
            if not paper_assigned.get(preferred_paper):
                paper_assigned[preferred_paper] = student
                students_assigned.add(student)

paper_by_name = {p[0]: p for p in paper_rows}
student_by_mail = {s[2]: s for s in student_rows}
writer = csv.writer(sys.stdout)
writer.writerow(["Name", "Email", "Legi", "Paper title", "Paper link"])
for paper in paper_rows:
    if paper_assigned[paper[0]] is None:
        continue
    student_details = student_by_mail[paper_assigned[paper[0]]]
    is_among_preferences = student_preferences[student_details[2]].index(paper[0])
    writer.writerow(student_details[1:4] + (is_among_preferences,) + paper_by_name[paper[0]] + student_details[9:11])
