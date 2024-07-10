# A.Привет, Яндекс!

print("Привет, Яндекс!")

# B.Привет, всем!

name = input("Как Вас зовут?")
print(f"Привет, {name}")

# C.Излишняя автоматизация

print(f"{input()}\n" * 3)

# D.Сдача

print(int(input()) - int(2.5 * 38))

# C.Магазин

price = int(input())
weight = int(input())
money = int(input())

print(money - price * weight)

# F.Чек

product = input()
price = int(input())
weight = int(input())
money = int(input())
cost = price * weight
change = money - price * weight

print(f'''Чек
{product} - {weight}кг - {price}руб/кг
Итого: {cost}руб
Внесено: {money}руб
Сдача: {change}руб''')

# G.Делу — время, потехе — час

print("Купи слона!\n" * int(input()))

# H.Наказание

amount = int(input())
phrase = input()

print(f'Я больше никогда не буду писать "{phrase}"!\n' * amount)

# I.Деловая колбаса

duration = int(input())
amount_of_children = int(input())
speed = 0.5

print(int(duration * amount_of_children * speed))

# J.Детский сад — штаны на лямках

child_name = input()
locker_num = int(input())
group_num = locker_num // 100
bed_num = locker_num // 10 % 10
child_num = locker_num % 10

print(f"Группа №{group_num}.\n{child_num}. {child_name}.\nШкафчик: {locker_num}.\nКроватка: {bed_num}.")

# K.Автоматизация игры

initial_number = int(input())
a = initial_number // 1000
b = initial_number // 100 % 10
c = initial_number // 10 % 10
d = initial_number % 10
result_number = int(str(b) + str(a) + str(d) + str(c))

print(result_number)

# L.Интересное сложение

num_1 = int(input())
num_2 = int(input())

a = (num_1 // 100 + num_2 // 100) % 10
b = (num_1 // 10 + num_2 // 10) % 10
c = (num_1 + num_2) % 10

print(a * 100 + b * 10 + c)

# M.Дед Мороз и конфеты

num_children = int(input())
num_candies = int(input())
print(num_candies // num_children, num_candies % num_children, sep='\n')

# N.Шарики и ручки

red_balls = int(input())
green_balls = int(input())
blue_balls = int(input())

print(red_balls + blue_balls + 1)

# O.В ожидании доставки

n = int(input())
m = int(input())
t = int(input())
delivery_time = n * 60 + m + t
print(f"{delivery_time // 60 % 24:0>2}:{delivery_time % 60:0>2}")

# P.Доставка

warehouse_location = int(input())
store_location = int(input())
avg_speed = int(input())

delivery_time = (store_location - warehouse_location) / avg_speed
print(f"{delivery_time:.2f}")

# Q.Ошибка кассового аппарата

sales = int(input())
last_sale = int(input(), 2)

print(sales + last_sale)

# R.Сдача 10

cost = int(input(), 2)
money = int(input())

print(money - cost)

# S.Украшение чека

product = input()
price = int(input())
weight = int(input())
cash = int(input())

cost = price * weight
change = cash - cost

print(f"{'Чек':=^35}")
print(f"Товар:{product:>29}")
print(f"Цена:{f'{weight}кг * {price}руб/кг':>30}")
print(f"Итого:{f'{cost}руб':>29}")
print(f"Внесено:{f'{cash}руб':>27}")
print(f"Сдача:{f'{change}руб':>29}")
print(f'{"":=^35}')

# T.Мухи отдельно, котлеты отдельно

total_weight = int(input())
total_price = int(input())
price1 = int(input())
price2 = int(input())

weight1 = total_weight * (total_price - price2) // (price1 - price2)
weight2 = total_weight - weight1

print(weight1, weight2)