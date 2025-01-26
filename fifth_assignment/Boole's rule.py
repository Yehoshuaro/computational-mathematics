import math
def booles_rule_integral(a, b, f):
    h = (b - a) / 5

    x0 = a
    x1 = a + h
    x2 = a + 2 * h
    x3 = a + 3 * h
    x4 = b

    f0 = f(x0)
    f1 = f(x1)
    f2 = f(x2)
    f3 = f(x3)
    f4 = f(x4)

    integral = (2 * h / 45) * (7 * f0 + 32 * f1 + 12 * f2 + 32 * f3 + 7 * f4)
    return integral

def function(x):
    return math.sqrt(math.sin(x))
a = 0
b = math.pi / 2

result = booles_rule_integral(a, b, function)
print("Approximated integral:", result)
