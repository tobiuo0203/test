import csv
import pprint

with open('Book3.csv') as f:
    reader = csv.reader(f)
    l = [row for row in reader]
print(l)

print(l[1][1])