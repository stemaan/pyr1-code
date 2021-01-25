import csv

with open('adresy.csv') as f:
    reader = csv.DictReader(f, delimiter=';')
    for l in reader:
        print(l.keys())
