def gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2

    return num1

print(gcd(5, 0))