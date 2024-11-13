class Fraction:
    def __init__(self, *numbers):
        if isinstance(numbers[0], str):
            num, denom = (int(num) for num in numbers[0].split('/'))
        else:
            num, denom = numbers
        self._numerator, self._denominator = num, denom
        self._is_negative = False
        self.__gcd_check()
        self.__check_negative()

    def numerator(self, num=None):
        if num:
            self._numerator = num
            self.__gcd_check()
            self.__check_negative()
        else:
            return self._numerator

    def denominator(self, num=None):
        if num:
            self._denominator = num
            self.__gcd_check()
            self.__check_negative()
        else:
            return self._denominator

    def __str__(self):
        return f'{self._is_negative * '-'}{self._numerator}/{self._denominator}'

    def __repr__(self):
        return f'Fraction({self._is_negative * '-'}{self._numerator}, {self._denominator})'

    def __gcd_check(self):
        num1, num2 = self._numerator, self._denominator
        while num2:
            num1, num2 = num2, num1 % num2
        gcd = num1
        self._numerator //= gcd
        self._denominator //= gcd

    def __check_negative(self):
        if (self._numerator < 0) != (self._denominator < 0):
            self._is_negative = True
        self._numerator = abs(self._numerator)
        self._denominator = abs(self._denominator)

    def __neg__(self):
        return Fraction(-self.numerator(), self.denominator())


# a = Fraction(1, 3)
# b = Fraction(-2, -6)
# c = Fraction(-3, 9)
# d = Fraction(4, -12)
# print(a, b, c, d)
# print(*map(repr, (a, b, c, d)))


a = Fraction('-1/2')
b = -a
print(a, b, a is b)
b.numerator(-b.numerator())
a.denominator(-3)
print(a, b)
print(a.numerator(), a.denominator())
print(b.numerator(), b.denominator())

# print(Fraction('-4/2'))
