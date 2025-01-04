import numpy as np


def stairs(vektor):
    matrix = vektor + np.zeros((vektor.size, 1), dtype='int8')
    for i in range(1, vektor.size):
        matrix[i] = np.concatenate((matrix[i][-i:], matrix[i][:-i]))

    return matrix


print(stairs(np.arange(5)))