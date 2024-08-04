cereal_lovers = {}

for _ in range(int(input())):
    name, cereals = input().split()
    for cereal in cereals:
        cereal_lovers[cereal] = cereal_lovers.get(cereals, []) + [name]

cereal_required = input()

list_of_cereal_lovers = sorted(cereal_lovers[cereal_required])

if list_of_cereal_lovers:
    for name in list_of_cereal_lovers:
        print(name)
else:
    print('Таких нет')
