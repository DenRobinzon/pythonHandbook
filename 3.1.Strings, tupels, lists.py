# A.Азбука

n = int(input())
is_correct = "YES"

for _ in range(n):
    word = input()
    if word[0] not in "абв":
        is_correct = "NO"
        break

print(is_correct)

# B.Кручу-верчу

text = input()
for char in text:
    print(char)

# C.Анонс новости

max_length = int(input())
n = int(input())

for _ in range(n):
    title = input()
    if len(title) <= max_length:
        print(title)
    else:
        print(f"{title[:(max_length - 3)]}...")

# D.Очистка данных

while (report := input()) != '':
    if report.endswith('@@@'):
        pass
    elif report.startswith('##'):
        print(report[2:])
    else:
        print(report)

# E.А роза упала на лапу Азора 4.0
text = input()

if text == text[::-1]:
    print("YES")
else:
    print("NO")

# F.Зайка — 6

bunnies = 0
for _ in range(int(input())):
    bunnies += input().lower().count('зайка')
print(bunnies)

# G.А и Б сидели на трубе

numbers = input().split()
summa = 0

print(int(numbers[0]) + int(numbers[1]))

# H.Зайка — 7

for _ in range(int(input())):
    if 'зайка' in (place := input()):
        print(place.find('зайка') + 1)
    else:
        print('Заек нет =(')

# I.Без комментариев

while (input_string := input()) != '':
    if input_string.startswith('#'):
        pass
    elif '#' in input_string:
        print(input_string[:input_string.index('#')])
    else:
        print(input_string)

# J.Частотный анализ на минималках

text = ''
letters = ''
best_letter = ''
best_result = 0
while (input_string := input()) != 'ФИНИШ':
    text += input_string.replace(' ', '').lower()

for letter in text:
    if letter not in letters:
        letters += letter
        if (result := text.count(letter)) > best_result:
            best_letter = letter
            best_result = result
        elif result == best_result and letter < best_letter:
            best_letter = letter

print(best_letter)

# K.Найдется всё
titles = []
for _ in range(int(input())):
    titles.append(input())

query = input()

for title in titles:
    if query.lower() in title.lower():
        print(title)

# L.Меню питания

days = int(input())
menu = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']

for i in range(days):
    print(menu[i % 5])

# M.Массовое возведение в степень

numbers = []

for _ in range(int(input())):
    numbers.append(int(input()))

power = int(input())

for number in numbers:
    print(number ** power)

# N.Массовое возведение в степень 2.0

numbers = input().split()
power = int(input())

for number in numbers:
    print(int(number) ** power, end=' ')

# O.НОД 3.0

numbers = input().split()
number1 = int(numbers[0])

for number2 in numbers[1:]:
    while number2:
        number2 = int(number2)
        number1, number2 = number2, number1 % number2

print(number1)

# P.Анонс новости 2.0

title = ''
length = int(input())
lines = int(input())
short_title = None

for i in range(lines):
    title += input()

    if (not short_title) and len(title) - i >= length - 3:
        short_title = title[:length + i - 3] + '...'

    if i == lines - 1 and len(title) - i <= length:
        short_title = title.rstrip('\n')

    title += '\n'

print(short_title)

# Q.А роза упала на лапу Азора 5.0

text = input().replace(' ', '').lower()

if text == text[::-1]:
    print('YES')
else:
    print('NO')


# R.RLE

numbers = input()
current_number = None
counter = 0

for number in numbers:
    if not current_number:
        current_number = number

    if current_number != number:
        print(current_number, counter)
        current_number = number
        counter = 1
    else:
        counter += 1

print(current_number, counter)

# S.Польский калькулятор

input_data = input().split()
numbers = []

for i in input_data:
    if i.isdigit():
        numbers.append(int(i))
    else:
        match i:
            case '*':
                numbers.append(numbers.pop() * numbers.pop())
            case '-':
                numbers.append(numbers.pop(-2) - numbers.pop())
            case '+':
                numbers.append(numbers.pop() + numbers.pop())
            case '/':
                numbers.append(numbers.pop(-2) - numbers.pop())

print(numbers[0])

# T.Польский калькулятор — 2

input_data = input().split()
numbers = []

for i in input_data:
    if i.lstrip('-').isdigit():
        numbers.append(int(i))
    else:
        match i:
            case '*':
                numbers.append(numbers.pop() * numbers.pop())
            case '-':
                numbers.append(numbers.pop(-2) - numbers.pop())
            case '+':
                numbers.append(numbers.pop() + numbers.pop())
            case '/':
                numbers.append(numbers.pop(-2) // numbers.pop())
            case '~':
                numbers[-1] = -numbers[-1]
            case '!':
                number = numbers[-1]
                factorial = 1
                for j in range(2, number + 1):
                    factorial *= j
                numbers[-1] = factorial
            case '#':
                numbers.append(numbers[-1])
            case '@':
                numbers[-3], numbers[-2], numbers[-1] = numbers[-2], numbers[-1], numbers[-3]

print(numbers[0])