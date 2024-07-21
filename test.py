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





