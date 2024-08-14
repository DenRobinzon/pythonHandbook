# A.Список квадратов
[num ** 2 for num in range(a, b + 1)]

# B.Таблица умножения 2.0
[[num1 * num2 for num2 in range(1, n + 1)] for num1 in range(1, n + 1)]

# C.Длины всех слов
[len(word) for word in sentence.split()]

# D.Множество нечетных чисел
{num for num in set(numbers) if num % 2}

# E.Множество всех полных квадратов
{num for num in numbers if num ** 0.5 == int(num ** 0.5)}

# F.Буквенная статистика
{num: [div for div in range(1, num + 1) if not num % div] for num in numbers}

# G.Делители
{num: [div for div in range(1, num + 1) if not num % div] for num in numbers}

# H.Аббревиатура
''.join(word[0].upper() for word in string.split())

# I.Преобразование в строку
' - '.join(str(num) for num in sorted(set(numbers)))

# J.RLE наоборот
''.join(char * number for char, number in rle)