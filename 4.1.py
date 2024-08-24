# 4.1. Функции. Области видимости. Передача параметров в функции
# A.Функциональное приветствие
def print_hello(name):
    print(f'Hello, {name}!')

# B.Функциональный НОД
def gcd(number1, number2):
    while number2:
        number1, number2 = number2, number1 % number2
    return number1

# C.Длина числа
def number_length(number):
    return len(str(number).lstrip('-'))

# D.Имя of the month
def month(number, language):
    months = {'en': ['January', 'February', 'March',
                     'April', 'May', 'June',
                     'July', 'August', 'September',
                     'October', 'November', 'December'],
              'ru': ['Январь', 'Февраль', 'Март',
                     'Апрель', 'Май', 'Июнь',
                     'Июль', 'Август', 'Сентябрь',
                     'Октябрь', 'Ноябрь', 'Декабрь']}
    return months[language][number - 1]

# E.Числовая строка
def fun(line):
    return tuple(int(num) for num in line.split())

# F.Модернизация системы вывода
old_lines = set()


def modern_print(line):
    if line not in old_lines:
        print(line)
        old_lines.add(line)

# G.Шахматный «обед»
def can_eat(coordinates1, coordinates2):
    x1, y1 = coordinates1
    x2, y2 = coordinates2
    return abs(x2 - x1) + abs(y2 - y1) == 3 and abs(abs(x2 - x1) - abs(y2 - y1)) == 1
# f а это подсмотрел, оно лаконичнее
def can_eat(coordinates1, coordinates2):
    x1, y1 = coordinates1
    x2, y2 = coordinates2
    return {abs(x2 - x1), abs(y2 - y1)} == {1, 2}

# H.А роза упала на лапу Азора 7.0
def is_palindrome(object):
    if type(object) is int:
        object = str(object)
    return object == object[::-1]

# I.Простая задача 5.0
def is_prime(number):
    prime = True
    if number < 2:
        prime = False
    else:
        for divider in range(2, int(number ** 0.5) + 1):
            if number % divider == 0:
                prime = False
                break
    return prime

# J.Слияние
def merge(numbers1, numbers2):
    numbers = list(numbers1 + numbers2)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                is_sorted = False
    return numbers

# а это подсмотрел
def merge(numbers1, numbers2):
    numbers1, numbers2 = list(numbers1), list(numbers2)
    i1, i2 = 0, 0
    numbers = []
    while i1 < len(numbers1) and i2 < len(numbers2):
        if numbers1[i1] < numbers2[i2]:
            numbers.append(numbers1[i1])
            i1 += 1
        else:
            numbers.append(numbers2[i2])
            i2 += 1
    numbers.extend(numbers1[i1:])
    numbers.extend(numbers2[i2:])
    return tuple(numbers)

# K.
# L.
# M.
# N.
# O.
# P.
# Q.
# R.
# S.
# T.