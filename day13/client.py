class Person:
    def __init__(self, firstname, lastname, id):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Client(Person):
    clients_quantity = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Client.clients_quantity += 1
        self.client_id = Client.clients_quantity

    def __str__(self):
        full_name = super().__str__()
        return f"{self.client_id} " + full_name


if __name__ == '__main__':
    client1 = Client('Jan', 'Kowalski', 123123123)
