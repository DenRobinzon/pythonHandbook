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








