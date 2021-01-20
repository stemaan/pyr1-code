# def foo(value, my_list=[]):
#     my_list.append(value)
#     return my_list

def foo(value, my_list=None):
    if my_list is None: # a = 3 b = 3 vs a == b, a is b
        my_list = []
    my_list.append(value)
    return my_list


print(foo(1, [2, 3]))
print(foo(5))
print(foo(3, [99, 999, 9999]))
print(foo(4))
print(foo(9, [1]))
print(foo(55))
