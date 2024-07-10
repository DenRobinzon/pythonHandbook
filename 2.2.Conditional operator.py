# A.Просто здравствуй, просто как дела

name = input("Как Вас зовут?\n")
print(f"Здравствуйте, {name}!")
state = input("Как дела?\n")
match state:
    case "хорошо":
        print("Я за вас рада!")
    case "плохо":
        print("Всё наладится!")

# B.Кто быстрее?

speed_petya = int(input())
speed_vasya = int(input())
if speed_petya > speed_vasya:
    print("Петя")
else:
    print("Вася")

# C.Кто быстрее на этот раз?

speed_petya = int(input())
speed_vasya = int(input())
speed_tolya = int(input())

if speed_petya > speed_vasya:
    if speed_petya > speed_tolya:
        print("Петя")
    else:
        print("Толя")
else:
    if speed_vasya > speed_tolya:
        print("Вася")
    else:
        print("Толя")

# D.Список победителей

speed_petya = int(input())
speed_vasya = int(input())
speed_tolya = int(input())

if speed_petya > speed_vasya:
    if speed_petya > speed_tolya:
        if speed_vasya > speed_tolya:
            print("1. Петя\n2. Вася\n3. Толя")
        else:
            print("1. Петя\n2. Толя\n3. Вася")
    else:
        print("1. Толя\n2. Петя\n3. Вася")
else:
    if speed_vasya > speed_tolya:
        if speed_petya > speed_tolya:
            print("1. Вася\n2. Петя\n3. Толя")
        else:
            print("1. Вася\n2. Толя\n3. Петя")
    else:
        print("1. Толя\n2. Вася\n3. Петя")

# E.Яблоки

aplle_petya = int(input()) + 6
apple_vasya = int(input()) + 12

if aplle_petya > apple_vasya:
    print("Петя")
else:
    print("Вася")

# F.Сила прокрастинации

year = int(input())

if year % 400 == 0:
    print("YES")
elif year % 100 == 0:
    print("NO")
elif year % 4 == 0:
    print("YES")
else:
    print("NO")

# G.А роза упала на лапу Азора

number = int(input())

n1 = number // 1000
n2 = number % 1000 // 100
n3 = number % 100 // 10
n4 = number % 10

if n1 == n4 and n2 == n3:
    print("YES")
else:
    print("NO")

# H.Зайка — 1

landscape = input()

if "зайка" in landscape:
    print("YES")
else:
    print("NO")

# I.Первому игроку приготовиться

player1, player2, player3 = input(), input(), input()

if player1 < player2:
    if player1 < player3:
        print(player1)
    else:
        print(player3)
elif player2 < player3:
    print(player2)
else:
    print(player3)

# J.Лучшая защита — шифрование

number = int(input())

n1 = number // 100
n2 = number // 10 % 10
n3 = number % 10

sum1 = n1 + n2
sum2 = n2 + n3

if sum1 < sum2:
    print(f"{sum2}{sum1}")
else:
    print(f"{sum1}{sum2}")

# K.Красота спасёт мир

number = int(input())

n1 = number // 100
n2 = number // 10 % 10
n3 = number % 10

mx = max(n1, n2, n3)
mn = min(n1, n2, n3)
md = n1 + n2 + n3 - mn - mx

if mn + mx == md * 2:
    print('YES')
else:
    print('NO')

# L.Музыкальный инструмент

side1, side2, side3 = int(input()), int(input()), int(input())

total_sum = side1 + side2 + side3
max_side = max(side1, side2, side3)

if max_side >= total_sum - max_side:
    print("NO")
else:
    print("YES")

# M.Властелин Чисел: Братство общей цифры

num_elv, num_dwrf, num_hmn = int(input()), int(input()), int(input())

if num_elv % 10 == num_dwrf % 10 == num_hmn % 10:
    print(num_elv % 10)
elif num_elv // 10 == num_dwrf // 10 == num_hmn // 10:
    print(num_elv // 10)

# N.Властелин Чисел: Две Башни

number = int(input())

n1 = number // 100
n2 = number // 10 % 10
n3 = number % 10

n_max = max(n1, n2, n3)
n_min = min(n1, n2, n3)
n_mid = n1 + n2 + n3 - n_max - n_min

n_mag_max = n_max * 10 + n_mid

if n_min != 0:
    n_mag_min = n_min * 10 + n_mid
elif n_mid != 0:
    n_mag_min = n_mid * 10
else:
    n_mag_min = n_mag_max

print(n_mag_min, n_mag_max)

# O.Властелин Чисел: Возвращение Цезаря

num_1, num_2 = int(input()), int(input())

n1_1, n1_2 = num_1 // 10, num_1 % 10
n2_1, n2_2 = num_2 // 10, num_2 % 10
num_max = max(n1_1, n1_2, n2_1, n2_2)
num_min = min(n1_1, n1_2, n2_1, n2_2)
num_mid = (n1_1 + n1_2 + n2_1 + n2_2 - num_max - num_min) % 10

magic_number = num_max * 100 + num_mid * 10 + num_min
print(magic_number)

# P.Легенды велогонок возвращаются: кто быстрее?

speed_p, speed_v, speed_t = int(input()), int(input()), int(input())

if speed_p > speed_v and speed_p > speed_t:
    first = "Петя"
    if speed_v > speed_t:
        second = "Вася"
        third = "Толя"
    else:
        second = "Толя"
        third = "Вася"
elif speed_v > speed_p and speed_v > speed_t:
    first = "Вася"
    if speed_p > speed_t:
        second = "Петя"
        third = "Толя"
    else:
        second = "Толя"
        third = "Петя"
if speed_t > speed_v and speed_t > speed_p:
    first = "Толя"
    if speed_v > speed_p:
        second = "Вася"
        third = "Петя"
    else:
        second = "Петя"
        third = "Вася"
print(f"{first:^24}")
print(f"{second:^8}{'':^16}")
print(f"{'':^16}{third:^8}")
print(f"{'II':^8}{'I':^8}{'III':^8}")

# Q.Корень зла
# надо еще подумать

a, b, c = float(input()), float(input()), float(input())

if a == 0:
    if b == 0:
        if c == 0:
            print("Infinite solutions")
        else:
            print("No solutions")
    else:
        x1 = -c / b
        print(x1)
elif b == c == 0:
    print("0.00")
elif c == 0:
    x1 = 0
    x2 = -b / a
    print(f"{min(x1, x2):.2f} {max(x1, x2):.2f}")
else:
    d = b ** 2 - 4 * a * c
    if d < 0:
        print("No solutions")
    elif d == 0:
        x = -b / (2 * a)
        if x != 0:
            print(f"{x:.2f}")
    elif d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print(f"{min(x1, x2):.2f} {max(x1, x2):.2f}")