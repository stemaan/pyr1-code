digit = int(input("Podaj liczbe: "))

# 1. jesli zmienna jest wieksza od 0 wyswietl "{wartosc_zmiennej} jest wieksze od 0"
# 2. jesli zmienna jest mniejsza od 0 "{wartosc_zmiennej} jest mniejsze od 0"
# 3. wyswietl "podales zero!"

#
# if digit > 0:
#     print(f"{digit} jest wieksze od 0")
# elif digit < 0:
#     print(f"{digit} jest mniejsze od 0")
# else:
#     print("podałeś zero!")
#
# if digit % 2:
#     print(f'{digit} jest nieparzysta')
# else:
#     print(f'{digit} jest parzysta')
#
# if digit != 0:
#     print(f'{digit} jest rozne od zera!')
#
# if digit >= 10:
#     print(f'{digit} jest wieksze od 10')
#

greater_than_zero = digit > 0
if digit % 2 and greater_than_zero:
    print('True')

if digit < 0 or digit % 3:
    print('yes!')

if not digit < 0:
    print('no!')
