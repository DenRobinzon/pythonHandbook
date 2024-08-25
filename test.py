in_stock = {'coffee': 4, 'milk': 4, 'cream': 0}


def order(*wishlist):
    recipes = {
        'Эспрессо': {'coffee': 1},
        'Капучино': {'coffee': 1, 'milk': 3},
        'Макиато': {'coffee': 2, 'milk': 1},
        'Кофе по-венски': {'coffee': 1, 'cream': 2},
        'Латте Макиато': {'coffee': 1, 'milk': 2, 'cream': 1},
        'Кон Панна': {'coffee': 1, 'cream': 1}
    }
    served_drink = None

    for drink in wishlist:
        in_stock_after = {}
        for ingridient in recipes[drink]:
            if recipes[drink][ingridient] <= in_stock[ingridient]:
                in_stock_after[ingridient] = in_stock[ingridient] - recipes[drink][ingridient]
            else:
                break
        else:
            in_stock.update(in_stock_after)
            served_drink = drink
            break

    return served_drink if served_drink else 'К сожалению, не можем предложить Вам напиток'


print(f'{in_stock=}')
print(order("Эспрессо"))
print(f'{in_stock=}')

print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
