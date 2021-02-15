class A:
    def __init__(self):
        self.attr1 = 1
        self.attr2 = 2

    def hello(self):
        print('Hello', self.attr1, self.attr2)

    def bye(self):
        print('Bye')


class B:
    def bye(self):
        print('Bye from B')

    def random_word(self):
        print('Python')


class C(A, B):
    pass


class D(B, A):
    pass


if __name__ == '__main__':
    print(C.__mro__)
    obj = C()
    obj.hello()
    obj.bye()
    obj.random_word()

    print('*' * 8)

    print(D.__mro__)
    obj2 = D()
    obj2.hello()
    obj2.bye()
    obj2.random_word()