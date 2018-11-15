import math


class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        if y == 0:
            raise ValueError("mianownik cant be 0!")
        self.x = int(x)
        self.y = int(y)

    def __str__(self):  # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return str(self.x)
        else:
            return str(self.x) + "/" + str(self.y)

    def __repr__(self):  # zwraca "Frac(x, y)"
        return "Frac(" + str(self.x) + ", " + str(self.y) + ")"

    @staticmethod
    def nwd(a, b):
        return math.gcd(a, b)

    @staticmethod
    def nww(a, b):
        return a * b / Frac.nwd(a, b)

    def __add__(self, other):  # frac1 + frac2
        x1 = self.x
        x2 = other.x
        y1 = self.y
        y2 = other.y

        wsp_mianownik = Frac.nww(y1, y2)

        x1 *= wsp_mianownik / y1
        x2 *= wsp_mianownik / y2

        return Frac(x1 + x2, wsp_mianownik)

    def __radd__(self, other):

        # FLOATY
        if isinstance(other, float):
            num = other.as_integer_ratio()
            return self + Frac(num[0], num[1])
        return self + Frac(other, 1)

    def __sub__(self, other):
        # frac1 - frac2
        x1 = self.x
        x2 = other.x
        y1 = self.y
        y2 = other.y

        wsp_mianownik = Frac.nww(y1, y2)

        x1 *= wsp_mianownik / y1
        x2 *= wsp_mianownik / y2

        return Frac(x1 - x2, wsp_mianownik)

    def __rsub__(self, other):
        return self - Frac(other, 1)

    def __mul__(self, other):  # frac1 * frac2
        return Frac(self.x * other.x, self.y * other.y)

    def __rmul__(self, other):
        return self * Frac(other, 1)

    def __truediv__(self, other):
        # frac1 / frac2
        if other.x == 0:
            raise ZeroDivisionError("Division by zero")

        return self * Frac(other.y, other.x)

    def __rtruediv__(self, other):
        return self * Frac(1, other)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __cmp__(self, other):  # cmp(frac1, frac2)
        if float(self) > float(other):
            return 1
        elif float(self) < float(other):
            return -1
        else:
            return 0

    def __float__(self):  # float(frac)
        return float(self.x / self.y)
