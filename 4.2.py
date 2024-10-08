# 4.2. Позиционные и именованные аргументы. Функции высших порядков. Лямбда-функции
# A.Генератор списков
def make_list(size, value=0):
    return [value for _ in range(size)]

# B.Генератор матриц
def make_matrix(size, value=0):
    if type(size) is int:
        size = size, size
    return [[value for _ in range(size[0])] for _ in range(size[1])]

# C.Функциональный нод 2.0
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

# подсмотрел
def gcd(*numbers):
    a, *tail = numbers
    for b in tail:
        while b:
            a, b = b, a % b
    return a

# D.Имя of the month 2.0
def month(number, languge='ru'):
    months = {'en': ['January', 'February', 'March',
                     'April', 'May', 'June',
                     'July', 'August', 'September',
                     'October', 'November', 'December'],
              'ru': ['Январь', 'Февраль', 'Март',
                     'Апрель', 'Май', 'Июнь',
                     'Июль', 'Август', 'Сентябрь',
                     'Октябрь', 'Ноябрь', 'Декабрь']}
    return months[languge][number - 1]

# E.Подготовка данных
def to_string(*data, sep=' ', end='\n'):
    return sep.join([str(element) for element in data]) + end

# F.Кофейня
def order(*wishlist):
    recipes = {
        'Эспрессо': {'coffee': 1},
        'Капучино': {'coffee': 1, 'milk': 3},
        'Макиато': {'coffee': 2, 'milk': 1},
        'Кофе по-венски': {'coffee': 1, 'cream': 2},
        'Латте Макиато': {'coffee': 1, 'milk': 2, 'cream': 1},
        'Кон Панна': {'coffee': 1, 'cream': 1}
    }
    served_drink = None

    for drink in wishlist:
        in_stock_after = {}
        for ingridient in recipes[drink]:
            if recipes[drink][ingridient] <= in_stock[ingridient]:
                in_stock_after[ingridient] = in_stock[ingridient] - recipes[drink][ingridient]
            else:
                break
        else:
            in_stock.update(in_stock_after)
            served_drink = drink
            break

    return served_drink if served_drink else 'К сожалению, не можем предложить Вам напиток'


# G.В эфире рубрика «Эксперименты»
results = []


def enter_results(*data):
    results.extend(data)


def get_sum():
    return round(sum(results[::2]), 2), round(sum(results[1::2]), 2)


def get_average():
    nums_1, nums_2 = results[::2], results[1::2]
    return round(sum(nums_1) / len(nums_1), 2), round(sum(nums_2) / len(nums_2), 2)

# H.Длинная сортировка
(len(line), line.lower())

# I.Чётная фильтрация
lambda num: not sum(int(digit) for digit in str(num)) % 2

# J.Ключевой секрет

import itertools


def secret_replace(text, **replaces):
    replaces_cycled = {k: itertools.cycle(v) for k, v in replaces.items()}
    text_decrypted = ''
    for ch in text:
        if ch in replaces_cycled:
            text_decrypted += next(replaces_cycled[ch])
        else:
            text_decrypted += ch
    return text_decrypted
