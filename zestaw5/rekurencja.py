def fibonacci(n):
    suma = 0
    l1 = 0
    l2 = 1
    for i in range(2, n + 1):
        suma = l1 + l2
        l1 = l2
        l2 = suma

    return suma

def factorial(n):
    suma = 1
    for i in range(1, n + 1):
        suma *= i

    return suma