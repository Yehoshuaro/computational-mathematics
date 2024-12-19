import math

def f(x):
    return math.exp(x) - x**2
# Here, I wrote e**x - x**2
def bisection(a, b, iteractions):
    for _ in range(iteractions):
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

a = -2
b = 0
iteractions = 7

find_the_root = bisection(a, b, iteractions)
print(find_the_root)