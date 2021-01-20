def add_numbers(a, b):
    print(a + b)


def detect_number_type(number):
    if number % 2:  # 3 % 2 -> 1 r 1 -> bool(1) -> True
        print(f'{number} jest nieparzysta')
    else:
        print(f'{number} jest parzysta')


def is_even(number):
    if number % 2:
        return False
    else:
        return True


print(__name__)
if __name__ == '__main__':
    print('Hello world!')
    x = 3
    y = 4
    z = 15
    add_numbers(x, y)

    detect_number_type(x)
    detect_number_type(y)

    alias = detect_number_type
    alias(10)

    my_list = [1, "asd", detect_number_type, detect_number_type(z)]
    print(my_list)

    if is_even(y):
        detect_number_type(y)
