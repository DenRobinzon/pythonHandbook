# A. Раз, два, три! Ёлочка, гори!

while input() != "Три!":
    print("Режим ожидания...")
print("Ёлочка, гори!")

# B.Зайка — 3

c = 0
while (words := input()) != "Приехали!":
    if "зайка" in words:
        c += 1
print(c)

# C.Считалочка

for i in range(int(input()), int(input()) + 1):
    print(i, end=" ")

# D.Считалочка 2.0

n1, n2 = int(input()), int(input())

if n2 > n1:
    for i in range(n1, n2 + 1):
        print(i, end=" ")
else:
    for i in range(n1, n2 - 1, -1):
        print(i, end=" ")

# E.Внимание! Акция!

total_cost = 0

while (cost := float(input())) != 0:
    if cost >= 500:
        cost *= 0.9
    total_cost += cost

print(total_cost)

# F.НОД

n1, n2 = int(input()), int(input())

n_max = max(n1, n2)
n_min = min(n1, n2)

while n_min != 0:
    n_max, n_min = n_min, n_max % n_min

print(n_max)

# G.НОК

n1, n2 = int(input()), int(input())

n_max = max(n1, n2)
n_min = min(n1, n2)

while n_min != 0:
    n_max, n_min = n_min, n_max % n_min

print(int(n1 * n2 / n_max))

# H.Излишняя автоматизация 2.0

data = input()
for _ in range(int(input())):
    print(data)

# I.Факториал

number = int(input())
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(factorial)

# J.Маршрут построен

x, y = 0, 0

while (direction := input()) != "СТОП":
    if direction == "СЕВЕР":
        y += int(input())
    elif direction == "ВОСТОК":
        x += int(input())
    elif direction == "ЮГ":
        y -= int(input())
    elif direction == "ЗАПАД":
        x -= int(input())

print(y, x, sep="\n")

# K.Цифровая сумма

number = int(input())
sum_of_digits = 0

while number:
    sum_of_digits += number % 10
    number //= 10

print(sum_of_digits)

# L.Сильная цифра

number = int(input())
max_digit = 0

while number:
    if max_digit < (n := number % 10):
        max_digit = n
    number //= 10

print(max_digit)

# M.Первому игроку приготовиться 2.0

n = int(input())
first_player = input()

for _ in range(n - 1):
    if (name := input()) < first_player:
        first_player = name

print(first_player)

# N.Простая задача

number = int(input())
is_prime = "YES"

if number == 1:
    is_prime = "NO"
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = "NO"
            break
print(is_prime)

# O.Зайка-4

number_of_places = int(input())
counter = 0

for _ in range(number_of_places):
    if "зайка" in input():
        counter += 1

print(counter)

# P.А роза упала на лапу Азора 2.0

number = int(input())
reverse_number = 0
test_number = number

while test_number:
    reverse_number = reverse_number * 10 + test_number % 10
    test_number //= 10

if number == reverse_number:
    print("YES")
else:
    print("NO")

# Q.Четная чистота

number = int(input())
number_without_even = 0
power = 0

while number:
    if (digit := number % 10) % 2 != 0:
        number_without_even += digit * (10 ** power)
        power += 1
    number //= 10

print(number_without_even)









