# napisz klase odwzorowujaca czlowieka
# stan wewnetrzny (atrybuty): imie, nazwisko, pesel, wiek
# intefrejs (metody):
#   metoday introduce -> "hej, jestem Jan Kowalski mam X lat"
#   metoda do wyswietlenia dokladniej daty urodzin (na podstawie nr pesel)
class Human:
    def __init__(self, firstname, lastname, id_number, age):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id_number
        self.age = age

    def introduce_yourself(self):
        print(f'Hej, jestem {self.firstname} {self.lastname} mam {self.age} lat(a)')

    def display_birthday(self):
        birthday = self.id[:6]
        year = birthday[:2]
        month = birthday[2:4]
        day = birthday[4:6]
        print(f'Moja data urodzenia to: {year}-{month}-{day}')


if __name__ == '__main__':
    man = Human('Jan', 'Kowalski', '70345678901', 44)
    woman = Human('Ewa', 'Kowalska', '80987654321', 30)

    man.introduce_yourself()
    man.display_birthday()
    woman.introduce_yourself()
    woman.display_birthday()

    print(dir(man))
    print(dir(Human))

    Human.display_birthday(man)

    print(Human.__dict__)
    print(man.__dict__)