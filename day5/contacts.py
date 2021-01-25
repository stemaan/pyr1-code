import csv
from pprint import pprint
from collections import defaultdict


with open('adresy.csv', 'r') as f:
    reader = csv.DictReader(f, delimiter=';')

    contacts = defaultdict(list)
    print(reader.fieldnames)
    for line in reader:
        contacts[line['nazwisko']].append(
            {
                'imie': line['imie'],
                'tel': line['numer'],
                'miasto': line['miasto'],
                'ulica': line['ulica'],
                'nr_domu': line['nr']
            }
        )

pprint(contacts)
