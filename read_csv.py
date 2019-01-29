import csv
import collections
import dateutil.parser

crimes = collections.Counter()

with open("data/Crimes.csv", "rt") as f:
    for row in csv.DictReader(f):
        if dateutil.parser.parse(row["Date"]).year == 2015:
            crimes[row["Primary Type"]] += 1

for c in crimes.most_common(5):
    print(f"{c[0]:16}: {c[1]:4}")
