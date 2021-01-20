numbers = [-11, 0, 1, 5, 100, 123, 77, 88, 99, 20]

has_elements = True

while has_elements:
    if numbers: # bool(numbers) -> True/False
        number = numbers.pop()
        print(number)
    else:
        has_elements = False