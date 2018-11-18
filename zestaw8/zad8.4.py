import math


def heron(a, b, c):
    if (a >= b + c) or (c >= a + b) or (b >= a + c):
        raise ValueError("To nie jest trojkat!")

    p = 1 / 2 * (a + b + c)
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


print("Pole = " + str(heron(3, 4, 5)))
