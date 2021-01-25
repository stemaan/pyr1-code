osoby = {
    "studenci": ["Ala", "Jan", "Ania"],
    "wykladowcy": ["doktor", "profesor"]
}

print(osoby['studenci'][1])
osoby['studenci'].append('Barbara')
print(osoby)

example = {
    # [1, 2]: "one two"
    (1, 2): "one two",
    None: 'None'
}
print((example))

# dodanie nowego klucza do slownika
osoby['dziekanat'] = 'Grazynka'
print(osoby)

# typo!
osoby.update(dzieknat='Bozenka')
print(osoby)

osoby['dziekanat'] = 'Halyna'
print(osoby)

# wyswietlenie samych kluczy w slowniku
keys = osoby.keys()
print(keys)

# wyswietlenie tylko wartosci ze slownika
values = osoby.values()
print(values)

for key, values in osoby.items(): # 100
    print('key', key)
    for value in values: # 100
        print('value', value)

print('*'*80)
# klucze slownika
for key in osoby:
    print('key', key)
    # wartosci pod danym kluczem
    for value in osoby[key]:
        print('value', value)
