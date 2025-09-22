import csv
from datetime import datetime
import sys

# Read the CSV file
filename = sys.argv[1]
rows = []
with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if any(row[0].startswith(s) for s in ("Lab", "By Lab")) or not row[0]:
            # skip headers
            continue
        rows.append(row)

# Read the assignment file
assignments = {}
filename = sys.argv[2]
assignments = {}
with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if any(row[0].startswith(s) for s in ("Name")) or not row[0]:
            # skip headers
            continue
        assignments[row[5].strip()] = row[0]
LAB, TITLE, VENUE, TA, PAPER_URL, DATE, TA_MAIL = range(7)

# Parse dates and sort the entries by date
for row in rows:
    row[DATE] = datetime.strptime(row[DATE].strip(), '%d.%m.%Y')
rows.sort(key=lambda x: x[DATE])

# Generate HTML table rows
table_rows = []
for i, row in enumerate(rows):
    date = row[DATE].strftime('%d %b') if i % 2 == 0 else ""
    paper_link = f'<a href="{row[PAPER_URL]}">{row[TITLE]}</a>' if row[PAPER_URL].strip().startswith("http") else row[TITLE]
    ta = f'<a href="mailto:{row[TA_MAIL]}">{row[TA].split(" ")[0]}</a>'
    venue = row[VENUE]
    presenter = assignments.get(row[TITLE], "TBD")
    table_row = f"<tr><td>{date}</td><td>{paper_link}</td><td>{presenter}</td><td>{venue}</td><td>{ta}</td></tr>\n"
    table_rows.append(table_row)

# Print the HTML table rows
html_output = '\n'.join(table_rows)
print(html_output)