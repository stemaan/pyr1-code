def foo(value, my_list=None):
    if my_list is None:  # a = 3 b = 3 vs a == b, a is b
        my_list = []
    my_list.append(value)
    return my_list


print(foo(4))
value = 3
print(value)
nothing = None


def bar(a, b):
    print(a, b, nothing)


bar(1, 2)
# boom zly zakres zmiennych
#print(a)