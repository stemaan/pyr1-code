class Human:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value.lower()


class Jira:
    def __init__(self, *args, **kwargs):
        self.field123123123123 = 'something'

    def get_report(self):
        print('Approved by manager', self.approved_by_manager)

    @property
    def approved_by_manager(self):
        return self.field123123123123


if __name__ == '__main__':
    adam = Human('Adam')
    print(adam.name)
    adam.name = 'Jan'
    print(adam.name)
    form_username = 'form .username'
    data_to_submit = {
        form_username: 'jan',
        'password': 'admin1',
        'email': 'test@example.com'
    }
