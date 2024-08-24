from functools import reduce

def gcd_for_2(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1

def gcd(*numbers):
    return reduce(gcd_for_2, numbers)

print(gcd(6))