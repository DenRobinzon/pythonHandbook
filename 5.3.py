# A.Обработка ошибок
try:
    func()
except ValueError:
    print('ValueError')
except TypeError:
    print('TypeError')
except SystemError:
    print('SystemError')
else:
    print('No Exceptions')

# B.Ломать — не строить
func((), '2')
# C.Полное решение
# Ломать — не строить 2
class Bad:
    def __repr__(self):
        return


print(func(Bad()))

# D.Контроль параметров

def only_positive_even_sum(number_1, number_2):
    if not all((isinstance(num, int) for num in (number_1, number_2))):
        raise TypeError
    if not all((num > 0 and num % 2 == 0 for num in (number_1, number_2))):
        raise ValueError
    return number_1 + number_2

# E.Слияние с проверкой
def merge(arg_1, arg_2):
    if not hasattr(arg_1, '__iter__') or not hasattr(arg_2, '__iter__'):
        raise StopIteration
    for i in range(len(values := (*arg_1, *arg_2)) - 1):
        if not type(values[i]) is type(values[i + 1]):
            raise TypeError
    for i in range(len(arg_1) - 1):
        if arg_1[i] > arg_1[i + 1]:
            raise ValueError
    for i in range(len(arg_2) - 1):
        if arg_2[i] > arg_2[i + 1]:
            raise ValueError

    list_1, list_2 = list(arg_1), list(arg_2)
    sorted_list = []
    while list_1 and list_2:
        if list_1[0] <= list_2[0]:
            sorted_list.append(list_1.pop(0))
        else:
            sorted_list.append(list_2.pop(0))
    sorted_list.extend(list_1 + list_2)

    return sorted_list

# F.Корень зла 2
class NoSolutionsError(Exception):
    pass


class InfiniteSolutionsError(Exception):
    pass


def find_roots(a, b, c):
    for i in (a, b, c):
        if not isinstance(i, (int, float)):
            raise TypeError

    if a == b == c == 0:
        raise InfiniteSolutionsError

    elif a == b == 0:
        raise NoSolutionsError

    elif a == 0:
        roots = ((-c / b),)

    else:
        d = b ** 2 - 4 * a * c
        if d < 0:
            raise NoSolutionsError

        else:
            roots = ((- b + d ** 0.5) / (2 * a), (- b - d ** 0.5) / (2 * a))

    return tuple(sorted(roots))


print(find_roots(1, 2, 1))

# G.Валидация имени
class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError
    for ch in name:
        if not (ord(ch) in range(1040, 1104) or ord(ch) == 1025):
            raise CyrillicError
    if name != name.capitalize():
        raise CapitalError

    return name

# H.Валидация имени пользователя
class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(name):
    if not isinstance(name, str):
        raise TypeError
    valid_chars = list(range(48, 58)) + list(range(65, 91)) + list(range(97, 123)) + [95]
    for ch in name:
        if ord(ch) not in valid_chars:
            raise BadCharacterError
    if name[0].isdigit():
        raise StartsWithDigitError

    return name
# I.Валидация пользователя
class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def username_validation(name):
    if not isinstance(name, str):
        raise TypeError
    for ch in name.lower():
        if ch not in 'abcdefghijklmnopqrstuvwxyz_1234567890':
            raise BadCharacterError
    if name[0].isdigit():
        raise StartsWithDigitError

    return name


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError
    for ch in name.lower():
        if ch not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            raise CyrillicError
    if name != name.capitalize():
        raise CapitalError

    return name


def user_validation(**kwargs):
    if tuple(kwargs.keys()) != ('last_name', 'first_name', 'username'):
        raise KeyError
    return {'last_name': name_validation(kwargs['last_name']), 'first_name': name_validation(kwargs['first_name']),
            'username': username_validation(kwargs['username'])}
# J.Валидация пароля
from hashlib import sha256


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


def password_validation(password, min_length=8,
                        possible_chars='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_',
                        at_least_one=str.isdigit):
    if not isinstance(password, str):
        raise TypeError
    if len(password) < min_length:
        raise MinLengthError
    if not all(ch in possible_chars for ch in password):
        raise PossibleCharError
    if not any(at_least_one(ch) for ch in password):
        raise NeedCharError
    return sha256(password.encode(encoding='UTF-8')).hexdigest()

