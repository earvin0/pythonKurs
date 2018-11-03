import math


def nwd(a, b):
    return math.gcd(a, b)


def nww(a, b):
    return a * b / nwd(a, b)


def add_sub_frac(frac1, frac2, operator):
    wsp_mianownik = nww(frac1[1], frac2[1])

    frac1[0] *= wsp_mianownik / frac1[1]
    frac2[0] *= wsp_mianownik / frac2[1]

    if operator == "+":
        licznik = frac1[0] + frac2[0]
    else:
        licznik = frac1[0] - frac2[0]

    return [licznik, wsp_mianownik]


def add_frac(frac1, frac2):
    wsp_mianownik = nww(frac1[1], frac2[1])

    frac1[0] *= wsp_mianownik / frac1[1]
    frac2[0] *= wsp_mianownik / frac2[1]

    licznik = frac1[0] + frac2[0]

    return [licznik, wsp_mianownik]


def sub_frac(frac1, frac2):
    wsp_mianownik = nww(frac1[1], frac2[1])

    frac1[0] *= wsp_mianownik / frac1[1]
    frac2[0] *= wsp_mianownik / frac2[1]

    licznik = frac1[0] - frac2[0]

    return [licznik, wsp_mianownik]


def mul_frac(frac1, frac2):

    return [frac1[0] * frac2[0], frac1[1] * frac2[1]]


def div_frac(frac1, frac2):

    return mul_frac([frac1[0], frac1[1]], [frac2[1], frac2[0]])


def is_positive(frac):

    return frac[0] * frac[1] >= 0


def is_zero(frac):

    return frac[0] == 0


def frac2float(frac):

    return frac[0] / frac[1]


def cmp_frac(frac1, frac2):
    f1 = frac2float(frac1)
    f2 = frac2float(frac2)
    if f1 > f2:
        return 1
    elif f1 < f2:
        return -1
    else:
        return 0
