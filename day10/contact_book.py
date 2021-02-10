class Person:
    def __init__(self, firstname, lastname, phone_number):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone_number

    def __str__(self):
        return f'{self.firstname} {self.lastname} {self.phone}'


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, person):
        self.contacts.append(person)

    def search(self, lastname):
        for person in self.contacts:
            if lastname == person.lastname: # person['lastname']
                return person

    def display_all(self):
        for contact in self.contacts:
            print(contact)


if __name__ == '__main__':
    jan = Person('Jan', 'Kowalski', 123123123)  # 'Jan Kowalski 123123123'
    jan2 = Person('Jan', 'Kowalski', 123121233)
    ewa = Person('Ewa', 'Nowak', 8080808080)
    adam = Person('Adam', 'Nowak', 123456789)
    pawel = Person('Pawel', 'Nowak', 123456789)
    piotr = Person('Piotr', 'Nowak', 123456789)
    anna = Person('Anna', 'Nowakowska', 123456789)
    # print(jan.firstname, jan.lastname, jan.phone)
    # print(ewa.firstname, ewa.lastname, ewa.phone)
    # print('*'*80)
    print(jan)
    print(ewa)

    ksiazka_telefoniczna = ContactBook()

    ksiazka_telefoniczna.add_contact(jan)
    ksiazka_telefoniczna.add_contact(ewa)
    ksiazka_telefoniczna.add_contact(adam)
    ksiazka_telefoniczna.add_contact(pawel)
    ksiazka_telefoniczna.add_contact(piotr)
    ksiazka_telefoniczna.add_contact(anna)




    print('*'*8)
    found = ksiazka_telefoniczna.search('Nowak')
    print(found)
    print('*'*8)

    ksiazka_telefoniczna.display_all()