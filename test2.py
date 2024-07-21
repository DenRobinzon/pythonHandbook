while (number := int(input())) != 1000:
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print(factorial)