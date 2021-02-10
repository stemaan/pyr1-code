import csv


class Person:
    def __init__(self, firstname, lastname, phone_number, city, street, street_nr):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone_number
        self.city = city
        self.street = street
        self.street_nr = street_nr

    def __str__(self):
        return f'{self.firstname} {self.lastname} tel: {self.phone}, {self.city} ul. {self.street} {self.street_nr}'


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, person):
        self.contacts.append(person)

    def search_by_lastname(self, lastname):
        found = []
        for person in self.contacts:
            if lastname == person.lastname:
                found.append(person)
        return found

    def search(self, lastname, city, street):
        found = []
        for person in self.contacts:
            if lastname == person.lastname and city == person.city and street == person.street:
                found.append(str(person))
        return found

    def display_all(self):
        for contact in self.contacts:
            print(contact)

    def sort(self, reverse=False):
        self.contacts.sort(key=lambda person: person.lastname, reverse=reverse)  # def ?(person): return person.lastname

    def from_csv(self, filename, delimiter=','):
        with open(filename, 'r') as contacts_file:
            reader = csv.DictReader(contacts_file, delimiter=delimiter)
            for person_data in reader:  # PERSON_DATA TO JEST ROW!
                contact = Person(
                    person_data['imie'],
                    person_data['nazwisko'],
                    person_data['numer'],
                    person_data['miasto'],
                    person_data['ulica'],
                    person_data['nr']
                )
                self.add_contact(contact)


if __name__ == '__main__':
    # jan = Person('Jan', 'Kowalski', 123123123)  # 'Jan Kowalski 123123123'
    # jan2 = Person('Jan', 'Kowalski', 123121233)
    # ewa = Person('Ewa', 'Nowak', 8080808080)
    # adam = Person('Adam', 'Zigi', 123456789)
    # pawel = Person('Pawel', 'Nowak', 123456789)
    # piotr = Person('Piotr', 'Nowak', 123456789)
    # anna = Person('Anna', 'Nowakowska', 123456789)

    # print(jan)
    # print(ewa)

    ksiazka_telefoniczna = ContactBook()

    # ksiazka_telefoniczna.add_contact(jan)
    # ksiazka_telefoniczna.add_contact(ewa)
    # ksiazka_telefoniczna.add_contact(adam)
    # ksiazka_telefoniczna.add_contact(pawel)
    # ksiazka_telefoniczna.add_contact(piotr)
    # ksiazka_telefoniczna.add_contact(anna)
    print('*' * 8)
    found = ksiazka_telefoniczna.search_by_lastname('Nowak')
    print('Zanleziono', found)
    print('*' * 8)

    ksiazka_telefoniczna.display_all()

    print('po sortowaniu')
    ksiazka_telefoniczna.sort()
    ksiazka_telefoniczna.display_all()

    print('po sortowaniu malejaco')
    ksiazka_telefoniczna.sort(reverse=True)
    ksiazka_telefoniczna.display_all()

    print('*' * 8)
    ksiazka_telefoniczna.from_csv('/Users/przemek/PycharmProjects/pyr1-code/day5/contacts.csv')
    ksiazka_telefoniczna.sort()
    ksiazka_telefoniczna.display_all()
