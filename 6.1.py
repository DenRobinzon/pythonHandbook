# A.Математика — круто, но это не точно

import math

x = float(input())

print(math.log(math.pow(x, 3 / 16), 32) + math.pow(x, math.cos(math.pi * x / (2 * math.e))) - pow(
    math.sin(x / math.pi), 2))

# B.Потоковый НОД
import sys
import math

for line in sys.stdin:
    print(math.gcd(*map(int, line.split())))


# C.Есть варианты?
import math

guests, seats = map(int, input().split())

variations = math.comb(guests, seats)
print(variations * seats // guests, variations)

# D.Среднее не арифметическое
import math

numbers = [float(i) for i in input().split()]

print(math.pow(math.prod(numbers), 1 / len(numbers)))

# E.Шаг навстречу
import math

deca_coordinates = [float(i) for i in input().split()]

pola_coordinates_pol = [float(i) for i in input().split()]

pola_coordinates = [pola_coordinates_pol[0] * math.cos(pola_coordinates_pol[1]),
                    pola_coordinates_pol[0] * math.sin(pola_coordinates_pol[1])]

print(math.dist(deca_coordinates, pola_coordinates))

# F.Матрица умножения
import numpy as np


def multiplication_matrix(size):
    matrix = np.array([[i * j for i in range(1, size + 1)] for j in range(1, size + 1)])
    return matrix
# G.Шахматная подготовка
import numpy as np


def make_board(size):
    return np.array([[(i + j + 1) % 2 for i in range(size)] for j in range(size)], dtype='int8')

# H.Числовая змейка 3.0
import numpy as np


def snake(width, height, direction='H'):
    if direction == 'V':
        width, height = height, width
    matrix = np.arange(1, width * height + 1, dtype='int16')
    matrix = matrix.reshape(height, width)
    for i in range(1, height, 2):
        matrix[i] = matrix[i][::-1]
    if direction == 'V':
        matrix = np.transpose(matrix)
    return matrix

# I.Вращение
import numpy as np


def rotate(matrix, angle):
    for i in range(angle // 90):
        matrix = np.rot90(matrix, -1)
    return matrix

# J.Лесенка
import numpy as np


def stairs(vektor):
    matrix = vektor + np.zeros((vektor.size, 1), dtype='int8')
    for i in range(1, vektor.size):
        matrix[i] = np.concatenate((matrix[i][-i:], matrix[i][:-i]))

    return matrix

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