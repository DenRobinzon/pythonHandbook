# A.Символическая выжимка

print(''.join(set(input())))

# B.Символическая разница

print(''.join(set(input()).intersection(set(input()))))

# C.Зайка — 8

objects = set()
for _ in range(int(input())):
    objects = objects.union(set(input().split()))

print('\n'.join(objects))

# D.Кашееды

semolina_lovers = set()
oatmeal_lovers = set()

number_sl, number_ol = int(input()), int(input())

for _ in range(number_sl):
    semolina_lovers.add(input())

for _ in range(number_ol):
    oatmeal_lovers.add(input())

both_lovers = semolina_lovers & oatmeal_lovers

if both_lovers:
    print(len(both_lovers))
else:
    print('Таких нет')

# E.Кашееды — 2

number_of_children = int(input()) + int(input())
one_lovers = set()

for _ in range(number_of_children):
    name = input()
    if name in one_lovers:
        one_lovers.remove(name)
    else:
        one_lovers.add(name)

if one_lovers:
    print(len(one_lovers))
else:
    print('Таких нет')

# E.Кашееды — 2 - математическое решение

n, m = int(input()), int(input())
names = set()
for _ in range(n + m):
    names.add(input())

k = len(names)

res = 2 * k - n - m

print(res if res else 'Таких нет')