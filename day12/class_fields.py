class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class Employee(Person):
    employees_quantity = 0
    annual_salary_increase = 0.1

    def __init__(self, firstname, lastname, email, salary, role):
        super().__init__(firstname, lastname)
        self.email = email
        self.salary = salary
        self.role = role
        Employee.employees_quantity += 1

    def __str__(self):
        parent_str = super().__str__()
        # [Developer - 15000] Przemyslaw Lalak (przemyslaw.lalak@xcaliber.com)
        return f'[{self.role} - {self.salary} PLN] ' + parent_str + f' ({self.email})'

    def get_annual_salary(self):
        return 12 * self.salary

    def send_meme_to_coworker(self, coworker):
        # laduje obrazk z dysku i wysyla na email kolegi/kolezanki z pracy
        print('Yooo, check this out! LOL')
        print('Sending file >>>> to', coworker.email)
        print('Sent')

    @classmethod
    def send_email_to_all_employees(cls):
        print(f'Sending mail to all employees, total: {cls.employees_quantity}')

    @classmethod
    def set_salary_increase(cls, value):
        if value >= 0.2:
            cls.annual_salary_increase = 0.2
        else:
            cls.annual_salary_increase = value

    def increase_salary(self):
        # Employee/Developer.annual_salary_increase
        self.salary = self.salary + self.__class__.annual_salary_increase * self.salary


class Developer(Employee):
    annual_salary_increase = 0.2

    def free_fruit_wednesdays(self):
        pass


class Tester(Employee):
    annual_salary_increase = 0.08


if __name__ == '__main__':
    print(Employee.employees_quantity)
    tester = Employee('Jan', 'Kowalski', 'jankowalski@example.com', 10000, 'QA')
    print(Employee.employees_quantity)

    admin = Employee('Adam', 'Nowak', 'jankowalski@example.com', 12000, 'SysAdmin')
    print(Employee.employees_quantity)

    developer = Employee('Anna', 'Kowalska', 'jankowalski@example.com', 15000, 'Developer')
    print(Employee.employees_quantity)
    print(tester.firstname)
    print(admin.firstname)
    print(tester)
    print(admin)
    print(developer)
    Employee.send_email_to_all_employees()
    print(admin.employees_quantity)
    Employee.employees_quantity = 10

    print(admin.employees_quantity)
    print(tester.employees_quantity)
    print(developer.employees_quantity)

    print(Employee.__dict__)
    print(admin.__dict__)

    # utworzenie atrybuty
    tester.employees_quantity = 11
    Employee.employees_quantity = 12
    # tester.something = 'asd'
    # tester.foo()

    print(tester.employees_quantity)
    print(admin.employees_quantity)
    print(developer.employees_quantity)
    print(Employee.employees_quantity)
    # print(admin.employees_quantity2)

    admin.send_meme_to_coworker(tester)

    print(Employee.annual_salary_increase)
    print(admin.salary)
    admin.increase_salary()
    print(admin.salary)

    Employee.set_salary_increase(0.15)
    print(tester.salary)
    print(developer.salary)

    tester.increase_salary()
    developer.increase_salary()
    print(tester.salary)
    print(developer.salary)

    pythonista = Developer('Pawel', 'Nowak', 'asdasd@asd.com', 20000, 'Senior Python Developer')
    print(pythonista.salary)
    pythonista.increase_salary()
    print(pythonista.salary)

    qa = Tester('Anna', 'Nowak', 'asda@asd.com', 123123, 'QA')
    qa.increase_salary()
