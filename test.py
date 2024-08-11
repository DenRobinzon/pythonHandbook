ingridients = set()
recipes = {}

for _ in range(int(input())):
    ingridients.add(input())

for _ in range(int(input())):
    dish = input()
    recipes[dish] = set()
    for _ in range(int(input())):
        recipes[dish].add(input())
    if not ingridients >= recipes[dish]:
        del recipes[dish]

if recipes:
    print(*sorted(recipes), sep='\n')
else:
    print('Готовить нечего')