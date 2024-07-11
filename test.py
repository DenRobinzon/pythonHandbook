numbers = input().split()
number1 = int(numbers[0])

for number2 in numbers[1:]:
    while number2:
        number2 = int(number2)
        number1, number2 = number2, number1 % number2

print(number1)





