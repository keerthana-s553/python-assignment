import csv
import math
with open('sales_24.csv', 'r') as infile, \
     open('sales_updated.csv', 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
    writer.writeheader()
    for row in reader:
        try:
            row['Amount'] = str(math.floor(float(row['Amount'])))
        except (ValueError, TypeError):
            pass
        writer.writerow(row)
