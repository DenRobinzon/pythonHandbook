# 4.3. Рекурсия. Декораторы. Генераторы

# A.Рекурсивный сумматор
def recursive_sum(*numbers):
    if not numbers:
        return 0
    return recursive_sum(*numbers[:-1]) + numbers[-1]

# B.Рекурсивный сумматор цифр
def recursive_digit_sum(number):
    if not number:
        return number
    return recursive_digit_sum(number // 10) + number % 10

# C.Многочлен N-ой степени
def make_equation(*coefficients):
    if len(coefficients) == 1:
        return coefficients[0]
    return f'({make_equation(*coefficients[:-1])}) * x + {coefficients[-1]}'

# D.Декор результата
def answer(func):
    def decorated(*args, **kwargs):
        return f'Результат функции: {func(*args, **kwargs)}'

    return decorated

# E.Накопление результата
def result_accumulator(func):
    results = []

    def decorated(*args, method='accumulate', **kwargs):
        nonlocal results
        if method == 'accumulate':
            results.append(func(*args, **kwargs))
        elif method == 'drop':
            results.append(func(*args, **kwargs))
            results_final = results[:]
            results = []
            return results_final

    return decorated

# F.Сортировка слиянием
def merge_sort(numbers):
    if len(numbers) == 1:
        return [numbers[0]]
    numbers_sorted = []
    mid = len(numbers) // 2
    nums_1 = merge_sort(numbers[:mid])
    nums_2 = merge_sort(numbers[mid:])
    while nums_1 and nums_2:
        if nums_1[0] < nums_2[0]:
            numbers_sorted.append(nums_1.pop(0))
        else:
            numbers_sorted.append(nums_2.pop(0))
    numbers_sorted.extend(nums_1 + nums_2)
    return numbers_sorted

# более эффективное решение без pop(0)

def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers

    numbers_sorted = []
    mid = len(numbers) // 2
    nums_1 = merge_sort(numbers[:mid])
    nums_2 = merge_sort(numbers[mid:])

    while nums_1 and nums_2:
        if nums_1[-1] > nums_2[-1]:
            numbers_sorted.append(nums_1.pop())
        else:
            numbers_sorted.append(nums_2.pop())
    numbers_sorted.extend((nums_1 + nums_2)[::-1])
    numbers_sorted = numbers_sorted[::-1]
    return numbers_sorted

# вроде как самое эффективное
def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers

    numbers_sorted = []
    i_1 = i_2 = 0
    mid = len(numbers) // 2
    nums_1 = merge_sort(numbers[:mid])
    nums_2 = merge_sort(numbers[mid:])

    while i_1 < len(nums_1) and i_2 < len(nums_2):
        if nums_1[i_1] < nums_2[i_2]:
            numbers_sorted.append(nums_1[i_1])
            i_1 += 1
        else:
            numbers_sorted.append(nums_2[i_2])
            i_2 += 1
    numbers_sorted.extend((nums_1[i_1:] + nums_2[i_2:]))
    return numbers_sorted

# G.Однотипность не порок
def same_type(func):
    def wrapper(*args, **kwargs):
        initial_type = type(args[0])
        for arg in args:
            if not type(arg) is initial_type:
                print('Обнаружены различные типы данных')
                return None
        return func(*args, **kwargs)
    return wrapper

# H.Генератор Фибоначчи
def fibonacci(number):
    fib_1, fib_2 = 0, 1
    for _ in range(number):
        yield fib_1
        fib_1, fib_2 = fib_2, fib_1 + fib_2

# I.Циклический генератор
def cycle(lst):
    index = 0
    length = len(lst)
    while True:
        yield lst[index % length]
        index += 1

# еще проще
def cycle(lst):
    while True:
        for item in lst:
            yield item

# J."Выпрямление" списка
def make_linear(lst):
    lst_linear = []
    for item in lst:
        if type(item) is list:
            lst_linear.extend(make_linear(item))
        else:
            lst_linear.append(item)
    return lst_linear

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