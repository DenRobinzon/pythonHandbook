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


fraction = Fraction(3, 9)
print(fraction, repr(fraction))
fraction = Fraction('7/14')
print(fraction, repr(fraction))

fraction = Fraction(3, 210)
print(fraction, repr(fraction))
fraction.numerator(10)
print(fraction.numerator(), fraction.denominator())
fraction.denominator(2)
print(fraction.numerator(), fraction.denominator())
