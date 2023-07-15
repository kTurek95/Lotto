from random import randint

my_numbers = {23, 7, 14, 32, 1, 45}
COUNTER = 0


def lotto_numbers():
    numbers = set()
    while len(numbers) < 6:
        random_number = randint(1, 50)
        numbers.add(random_number)
    return numbers


def compare_numbers():
    matched_numbers = 0
    for number in result:
        if number in my_numbers:
            matched_numbers += 1

    return matched_numbers


while True:
    COUNTER += 1
    result = lotto_numbers()
    compare_numbers()

    if result == my_numbers:
        print(f'Brawo trafiłeś 6 za {COUNTER} razem')
        break
    if compare_numbers() == 3:
        print(f'Brawo, trafiłeś 3 liczby za {COUNTER} razem')
