'''
Task 3. Fraction

Create a Fraction class, which will represent all basic arithmetic logic for fractions (+, -, /, *)
with appropriate checking and error handling
'''


class Fraction:
    def __init__(self, fr_number):
        self.fr_number = fr_number
        try:
            type(fr_number) == str
            if self.fr_number.count('/') > 1:
                print('Only simple fractions!')
                return
            elif self.fr_number.count('/') == 0:
                print('Use fractions!')
                return
            else:
                fr = self.fr_number.find('/')
                self.numerator = int(self.fr_number[:fr])
                self.denominator = int(self.fr_number[fr+1:])
                print(self)
        except:
            print('Use only str!')
            return

    def __str__(self):
        return Fraction.simplify_frac(self.numerator, self.denominator)
        # return 'Fraction({numerator}/{denominator})'.format(numerator=self.numerator, denominator=self.denominator)

    '''
    # [https://www.cyberforum.ru/python-beginners/thread2204609.html]
    def reduce_fraction(n, m):
        k = math.gcd(n, m)
        return (n//k, m//k)
    '''

    def simplify_frac(n, d):  # [https://quares.ru/?id=396813]
        i = 2
        while i < min(n, d) + 1:
            if n % i == 0 and d % i == 0:
                n = n // i
                d = d // i
            else:
                i += 1
        # return n, d
        if n == 0:
            return 0
        if d == 1:
            return str(n)
        if d == 0:
            return 'ZeroDivisionError!!!'
        return 'Fraction({numerator}/{denominator})'.format(numerator=str(n), denominator=str(d))

    def addition(first, second):
        numerator = first.numerator * second.denominator + \
            first.denominator * second.numerator
        denominator = first.denominator * second.denominator
        return Fraction.simplify_frac(numerator, denominator)

    def subtraction(first, second):
        numerator = first.numerator * second.denominator - \
            first.denominator * second.numerator
        denominator = first.denominator * second.denominator
        return Fraction.simplify_frac(numerator, denominator)

    def multiply(first, second):
        numerator = first.numerator * second.numerator
        denominator = first.denominator * second.denominator
        return Fraction.simplify_frac(numerator, denominator)

    def division(first, second):
        numerator = first.numerator * second.denominator
        denominator = first.denominator * second.numerator
        return Fraction.simplify_frac(numerator, denominator)


if __name__ == "__main__":
    x = Fraction('1/4')
    y = Fraction(1/4)
    w = Fraction('1/4/3')
    z = Fraction('143')
    a = Fraction('1/3')
    b = Fraction('3/9')
    print(Fraction.subtraction(a, b))
    print(Fraction.subtraction(b, a))
    print(Fraction.addition(a, b))
    print(Fraction.multiply(a, b))
    print(Fraction.division(a, b))
    c = Fraction('3/15')
    d = Fraction('4/6')
    e = Fraction('10/5')
    f = Fraction('9/7')
    g = Fraction('5/0')


'''
---output---
Fraction(1/4)
Use only str!
Only simple fractions!
Use fractions!
Fraction(1/3)
Fraction(1/3)
0
0
Fraction(2/3)
Fraction(1/9)
1
Fraction(1/5)
Fraction(2/3)
2
Fraction(9/7)
ZeroDivisionError!!!
'''
