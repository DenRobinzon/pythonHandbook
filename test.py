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
            if self._numerator < 0:
                num = -num
            self._numerator = num
            self.__gcd_check()

        else:
            return abs(self._numerator)

    def denominator(self, num=None):
        if num:
            self._denominator = num
            self.__gcd_check()
        else:
            return self._denominator

    def __str__(self):
        return f'{self._numerator}/{self._denominator}'

    def __repr__(self):
        return f"Fraction('{self._numerator}/{self._denominator}')"

    def __gcd_check(self):
        num1, num2 = self._numerator, self._denominator
        while num2:
            num1, num2 = num2, num1 % num2
        gcd = num1
        self._numerator //= gcd
        self._denominator //= gcd

    def __neg__(self):
        return Fraction(-self._numerator, self._denominator)

    def __add__(self, other):
        new_numerator = self._numerator * other._denominator + self._denominator * other._numerator
        new_denominator = self._denominator * other._denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self._numerator * other._denominator - self._denominator * other._numerator
        new_denominator = self._denominator * other._denominator
        return Fraction(new_numerator, new_denominator)

    def __iadd__(self, other):
        self._numerator = self._numerator * other._denominator + self._denominator * other._numerator
        self._denominator = self._denominator * other._denominator
        self.__gcd_check()
        return self

    def __isub__(self, other):
        self._numerator = self._numerator * other._denominator - self._denominator * other._numerator
        self._denominator = self._denominator * other._denominator
        self.__gcd_check()
        return self

a = Fraction(1, 3)
b = Fraction(1, 2)
c = a + b
print(a, b, c, a is c, b is c)

a = Fraction(1, 8)
c = b = Fraction(3, 8)
b -= a
print(a, b, c, b is c)
