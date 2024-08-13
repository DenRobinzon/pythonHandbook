mutually_prime_numbers = {}
numbers_n_dividers = {}
numbers = []
numbers_str = input().split('; ')

for number in numbers_str:
    numbers.append(int(number))
numbers.sort()

for number in numbers:
    numbers_n_dividers[number] = []
    for div in range(1, number + 1):
        if number % div == 0:
            numbers_n_dividers[number].append(div)

for number1 in numbers:
    mutually_prime_numbers[number1] = set()
    for number2 in numbers:
        if len(set(numbers_n_dividers[number1]) & set(numbers_n_dividers[number2])) == 1:
            mutually_prime_numbers[number1].add(number2)

for number in mutually_prime_numbers:
    if mutually_prime_numbers[number]:
        print(number, ' - ', sep='', end='')
        print(*sorted(mutually_prime_numbers[number]), sep=', ')

#print(numbers, numbers_n_dividers, mutually_prime_numbers, sep='\n')
