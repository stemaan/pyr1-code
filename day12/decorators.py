import time
import random


def add_numbers(a, b):
    random_wait_time = random.randint(1, 5)
    time.sleep(random_wait_time)
    return a + b


def substract_number(a, b):
    random_wait_time = random.randint(1, 5)
    time.sleep(random_wait_time)
    if a < b:
        return b - a
    else:
        return a - b


# funkcja przyjmująca inną funkcję i jej argumenty jako parametry - dekorator
def timer(func, a, b):
    time_before = time.time()
    result = func(a, b)
    print(result)
    time_after = time.time()
    print('Total time', time_after - time_before)


if __name__ == '__main__':
    # time_before = time.time()
    # print(add_numbers(10, 20))
    # time_after = time.time()
    # print('Total time', time_after - time_before)

    timer(substract_number, 20, 10)
