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

# D.
# E.
# F.
# G.
# H.
# I.
# J.
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