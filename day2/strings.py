name = "Ala ma kota"
name2 = 'Przemek'

print(name)
print(name2)

name3 = name + ' ' + name2
print(name3)

first_letter = name[0]
print(first_letter)

length = len(name)
print(length)


last_letter_index = length - 1
last_letter = name[last_letter_index]
print(last_letter)

# indexowanie wspak, zaczyna sie od -1 do -N gdzie N to dlugosc stringu
print(name[-1])

# slice    varbiable[start:end]
first_three_letters = name[:3]
print(first_three_letters)

whole_name = name[:]
print(whole_name)

print(name[-4:-1])

# [start:end:step]
every_2nd_letter = name[::2]
print(every_2nd_letter)

# brak index errora!
print(name[2:10])

# niedozwolone
# name[1] = 's'

name = name.replace('kota', 'psa')
print(name)