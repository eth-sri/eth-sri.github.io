import csv
from datetime import datetime
import sys

# Read the CSV file
filename = sys.argv[1]
rows = []
with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if any(row[0].startswith(s) for s in ("SRI", "AST", "Paper title")) or not row[0]:
            # skip headers
            continue
        rows.append(row)

# Parse dates and sort the entries by date
for row in rows:
    row[4] = datetime.strptime(row[4].strip(), '%d.%m.%y')
rows.sort(key=lambda x: x[4])

# Generate HTML table rows
table_rows = []
for i, row in enumerate(rows):
    date = row[4].strftime('%d %b') if i % 2 == 0 else ""
    paper_link = f'<a href="{row[3]}">{row[0]}</a>' if row[3].strip().startswith("http") else row[0]
    ta = f'<a href="mailto:{row[5]}">{row[2]}</a>'
    venue = row[1]
    table_row = f"<tr><td>{date}</td><td>{paper_link}</td><td>TBD</td><td>{venue}</td><td>{ta}</td></tr>\n"
    table_rows.append(table_row)

# Print the HTML table rows
html_output = '\n'.join(table_rows)
print(html_output)