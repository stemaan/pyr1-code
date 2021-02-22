def foo(*args):
    for arg in args:
        print(arg)


def bar(**kwargs):
    if 'x' in kwargs:
        print(kwargs['x'])


foo(1, 2, 3, 10, 'a', 'c')
bar(x=123, y=98, something="ala ma kota")


def add(a, b, *numbers):
    if not numbers:
        return a + b
    temp = list(numbers)
    temp.append(a)
    temp.append(b)
    return sum(temp)


print(add(1, 2, 3, 10))


def baz(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


baz(1, 2, 4, 5, 6, 67, 7, abc='ala ma kota', somtehing='acb123', x=123)
