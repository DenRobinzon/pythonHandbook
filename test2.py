in_stock = {'coffee': 4, 'milk': 4, 'cream': 0}


def order(*args):
    res = 0
    rec = {
        "Эспрессо": {"coffee": 1},
        "Капучино": {"coffee": 1,
                     "milk": 3},
        "Макиато": {"coffee": 2,
                    "milk": 1},
        "Кофе по-венски": {"coffee": 1,
                           "cream": 2},
        "Латте Макиато": {"coffee": 1,
                          "milk": 2,
                          "cream": 1},
        "Кон Панна": {"coffee": 1,
                      "cream": 1},
    }
    for arg in args:
        flag = True
        for ing in rec[arg]:
            if in_stock[ing] < rec[arg][ing]:
                flag = False
                break
        if flag:
            res = arg
            for ing in rec[arg]:
                in_stock[ing] -= rec[arg][ing]
            break
    if res:
        return res
    else:
        return 'К сожалению, не можем предложить Вам напиток'


print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
