def solve1(a, b, c):
    if a == 0 and b == 0:
        raise ValueError("Obie wartosci sa zerowe!")
    elif a == 0:
        y = -c / b
        print("Prosta rownolegla do osi OX"+" y = " + str(y))
    elif b == 0:
        x = -c / a
        print("Prosta rownolegla do osi OY x = " + str(x))
    else:
        print("prosta postaci: ( r, "+str(-a/b)+" * r - "+str(c/b)+" )")


solve1(2, 2, 1)
solve1(2, 0, 1)
solve1(0, 2, 1)
