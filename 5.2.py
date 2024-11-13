# A.Классная точка 3.0
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def length(self, point):
        length = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        length = round(length, 2)
        return length


class PatchedPoint(Point):
    def __init__(self, *coordinates):
        if not coordinates:
            x = y = 0
        elif isinstance(coordinates[0], tuple):
            x, y = coordinates[0]
        else:
            x, y = coordinates
        super().__init__(x, y)

# B.Классная точка 4.0
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def length(self, point):
        length = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        length = round(length, 2)
        return length


class PatchedPoint(Point):
    def __init__(self, *coordinates):
        if not coordinates:
            x = y = 0
        elif isinstance(coordinates[0], tuple):
            x, y = coordinates[0]
        else:
            x, y = coordinates
        super().__init__(x, y)

    def __str__(self):
        return f'{self.x, self.y}'

    def __repr__(self):
        return f'PatchedPoint{self.x, self.y}'

# C.Классная точка 5.0
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def length(self, point):
        length = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        length = round(length, 2)
        return length


class PatchedPoint(Point):
    def __init__(self, *coordinates):
        if not coordinates:
            x = y = 0
        elif isinstance(coordinates[0], tuple):
            x, y = coordinates[0]
        else:
            x, y = coordinates
        super().__init__(x, y)

    def __str__(self):
        return f'{self.x, self.y}'

    def __repr__(self):
        return f'PatchedPoint{self.x, self.y}'

    def __add__(self, coordinates):
        return PatchedPoint(self.x + coordinates[0], self.y + coordinates[1])

    def __iadd__(self, coordinates):
        self.x += coordinates[0]
        self.y += coordinates[1]
        return self

# D.Дроби v0.1
class Fraction:
    def __init__(self, *numbers):
        if isinstance(numbers[0], str):
            num, denom = (int(num) for num in numbers[0].split('/'))
        else:
            num, denom = numbers
        self._numerator, self._denominator = num, denom
        self.__gcd_check()

    def numerator(self, num=None):
        if num:
            self._numerator = num
            self.__gcd_check()
        else:
            return self._numerator
        self.__gcd_check()

    def denominator(self, num=None):
        if num:
            self._denominator = num
            self.__gcd_check()
        else:
            return self._denominator
        self.__gcd_check()

    def __str__(self):
        return f'{self._numerator}/{self._denominator}'

    def __repr__(self):
        return f'Fraction({self._numerator}, {self._denominator})'

    def __gcd_check(self):
        num1, num2 = self._numerator, self._denominator
        while num2:
            num1, num2 = num2, num1 % num2
        gcd = num1
        self._numerator //= gcd
        self._denominator //= gcd

# E.Дроби v0.2

# F.
# G.
# H.
# I.
# J.
# K.
# L.
# M.
# N.
# O.
# P.
# Q.
# R.
# S.
# T.