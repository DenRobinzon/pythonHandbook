def gcd(*numbers):
    numbers = sorted(numbers)
    gcd_result = numbers[0]
    length = len(numbers)
    if length > 1:
        for i in range(length - 1):
            num2, num1 = gcd_result, numbers[i + 1]
            while num2:
                num1, num2 = num2, num1 % num2
            gcd_result = num1
    return gcd_result


print(gcd(1, 12, 48, 156, 10))
