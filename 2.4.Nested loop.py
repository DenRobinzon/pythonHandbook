# A.Таблица умножения
size = int(input())

for i in range(1, size + 1):
    for j in range(1, size + 1):
        print(i * j, end=' ')
    print()

# B.Не таблица умножения

size_of_table = int(input())

for i in range(1, size_of_table + 1):
    for j in range(1, size_of_table + 1):
        print(f"{j} * {i} = {j * i}")


# C.Новогоднее настроение

number = int(input())
k = 1
m = 1

while k <= number:
    for i in range(m):
        if k > number:
            break
        print(k, end=" ")
        k += 1
    if k <= number:
        print()
    m += 1

# C.Новогоднее настроение (в один цикл)

n = int(input())
m = 0
k = 0

for i in range(1, n + 1):
    print(i, end=" ")
    if m == k and i != n:
        print()
        k += 1
        m = 0
    else:
        m += 1

# D.Суммарная сумма

number_of_strings = int(input())
summa = 0

for _ in range(number_of_strings):
    new_number = int(input())
    while new_number:
        summa += new_number % 10
        new_number //= 10

print(summa)

# E.Зайка-5

n = int(input())
bunnies = 0

for _ in range(n):
    is_bunny = False
    while (place := input()) != "ВСЁ":
        if not is_bunny and "зайка" in place:
            bunnies += 1
            is_bunny = True

print(bunnies)

# F.НОД 2.0

n = int(input())
number1 = int(input())
nod = 1

for _ in range(n - 1):
    number2 = int(input())
    num_max = max(number1, number2)
    num_min = min(number1, number2)
    while num_min:
        num_max, num_min = num_min, num_max % num_min
    number1 = num_max

print(number1)

# G.На старт! Внимание! Марш!

number_of_cyclists = int(input())
initial_start_time = 3

for i in range(1, number_of_cyclists + 1):
    for j in range(initial_start_time, 0, -1):
        print(f"До старта {j} секунд(ы)")
    print(f"Старт {i}!!!")
    initial_start_time += 1

# H.Максимальная сумма

number_of_children = int(input())
champ = None
best_sum = 0

for _ in range(number_of_children):
    name = input()
    num = int(input())
    summa = 0
    while num:
        summa += num % 10
        num //= 10
    if best_sum <= summa:
        champ = name
        best_sum = summa
print(champ)

# I.Большое число

number_of_children = int(input())
champ = None
best_sum = 0

for _ in range(number_of_children):
    name = input()
    num = int(input())
    summa = 0
    while num:
        summa += num % 10
        num //= 10
    if best_sum <= summa:
        champ = name
        best_sum = summa
print(champ)

# J.Мы делили апельсин

number = int(input())

print('А Б В')
for i in range(1, number - 1):
    for j in range(1, number - i):
        k = number - i - j
        print(f"{i} {j} {k}")

# K.Простая задача 3.0

n = int(input())
num_of_primes = 0

for _ in range(n):
    number = int(input())
    if number > 1:
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        num_of_primes += is_prime
print(num_of_primes)

# L.Числовой прямоугольник

height, width = int(input()), int(input())
num = 1
cell_width = len(str(height * width))

for _ in range(height):
    for _ in range(width):
        print(f'{num:>{cell_width}}', end=' ')
        num += 1
    print()

# M.Числовой прямоугольник 2.0

height, width = int(input()), int(input())
cell_width = len(str(height * width))

for i in range(height):
    num = i + 1
    for j in range(width):
        print(f'{num:>{cell_width}}', end=' ')
        num += height
    print()

# N.Числовая змейка

height, width = int(input()), int(input())
cell_width = len(str(height * width))
is_even_string = True

for i in range(height):
    for j in range(1, width + 1):
        if is_even_string:
            print(f"{i * width + j:>{cell_width}}", end=" ")
        else:
            print(f"{i * width + width - j + 1:>{cell_width}}", end=" ")
    is_even_string = not is_even_string
    print()

# O.Числовая змейка 2.0

height, width = int(input()), int(input())
cell_width = len(str(height * width))

for row in range(height):
    for column in range(width):
        if column % 2 == 0:
            print(f"{column * height + row + 1:>{cell_width}}", end=" ")
        else:
            print(f"{column * height + height - row:>{cell_width}}", end=" ")

    print()

# P.Редизайн таблицы умножения

size = int(input())
cell_width = int(input())

for row in range(1, size + 1):
    for column in range(1, size + 1):
        print(f"{row * column:^{cell_width}}", end="")
        if column != size:
            print("|", end="")
    if row != size:
        print()
        print("-" * (size * (cell_width + 1) - 1))

# Q.А роза упала на лапу Азора 3.0

n = int(input())
palindromes = 0

for _ in range(n):
    number = int(input())
    is_palindrome = True
    test_number = number
    number_length = len(str(number))
    power = number_length - 1
    for i in range(number_length // 2):
        if test_number % 10 != test_number // (10 ** power):
            is_palindrome = False
            break
        test_number = test_number % (10 ** power) // 10
        power -= 2
    if is_palindrome:
        palindromes += 1

print(palindromes)

# Q.А роза упала на лапу Азора 3.0 - решение покороче

n = int(input())
palindromes = 0

for _ in range(n):
    number = int(input())
    reverse_number = 0
    test_number = number
    while test_number:
        reverse_number = reverse_number * 10 + test_number % 10
        test_number //= 10
    if number == reverse_number:
        palindromes += 1

print(palindromes)

# R.Новогоднее настроение 2.0
n = int(input())
num = 1
last_row = n
rows = 1
flag = False
row_width = 0

for i in range(n):
    row = ''
    for j in range(i + 1):
        if num > n:
            flag = True
            break
        if j == 0:
            row = f"{num}"
        else:
            row = f"{row} {num}"
        num += 1
    if len(row) > row_width:
        row_width = len(row)
    if flag:
        break

num = 1
flag = False

for i in range(n):
    row = ''
    for j in range(i + 1):
        if num > n:
            flag = True
            break
        if j == 0:
            row = f"{num}"
        else:
            row = f"{row} {num}"
        num += 1
    print(f"{row:^{row_width}}")
    if flag:
        break
