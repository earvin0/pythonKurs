import random
import math


def calc_pi(n):
    in_circle = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x * x + y * y <= 1:
            in_circle += 1
    my_pi = 4 * in_circle / n
    return my_pi


print(math.pi)
print(calc_pi(10000))
