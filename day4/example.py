numbers = [-11, 0, 1, 5, 100, 123, 77, 88, 99, 20]

for number in numbers:
    # check if number is odd
    if number % 2: # 3 % 2 -> 1 r 1 -> bool(1) -> True
        print(f'{number} jest nieparzysta')
    else:
        print(f'{number} jest parzysta')