def gcd(*numbers):
    a, *tail = numbers
    for b in tail:
        while b:
            a, b = b, a % b
    return a

print(gcd(1, 48, 156, 10))