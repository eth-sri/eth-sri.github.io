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

# Read the CSV file of student preferences
filename = sys.argv[2]
student_rows = []
with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if any(row[0].startswith(s) for s in ("Timestamp")) or not row[0]:
            # skip headers
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

for paper in paper_rows:
    print(f"{paper[0]}, {paper_assigned[paper[0]]}")
