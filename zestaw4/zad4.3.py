def factorial(n):
    suma = 1
    for i in range(1, n + 1):
        suma *= i

    return suma


print(factorial(5))
