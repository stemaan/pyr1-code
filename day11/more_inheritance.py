# TODO: utwórz hierarchię klas z klasą bazową User
# TODO: User (atrybuty) -> firstname, lastname, email, score
# TODO: User (metody) -> full_name()
class User:
    def __init__(self, firstname, lastname, email, score=0):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.score = score

    def full_name(self):
        return f'{self.firstname} {self.lastname} ({self.email})'


# TODO: utwórz klasę VipUser która dziedziczy po klasie User
# TODO: atrybuty pozostaja bez zmian
# TODO: korzystając z polimorfizmu nadpisz metodę full_name() -> '*USERNAME*'

class VipUser(User):
    def full_name(self):
        # old_text = super().full_name()
        # return '*' + old_text + '*'
        return f'*{self.firstname} {self.lastname} ({self.email})*'


class Admin(User):
    def delete_game(self, game_name):
        pass


class CasinoOperator(User):
    def modify_game(self, game_name):
        pass


if __name__ == '__main__':
    normal_user = User('Jan', 'Kowalski', 'jankowalski@example.com')
    vip = VipUser('Anna', 'Nowak', 'annanowak@example.com', 999999)

    print(normal_user.full_name())
    print(vip.full_name())

    print(isinstance(normal_user, User))
    print(isinstance(vip, User))
    print(isinstance(normal_user, VipUser))

    print(issubclass(VipUser, User))