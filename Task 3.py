""" (1 task of the 3rd Exercise)
def newton_raphson(x0, tol=0.001, max_iter=20):
    x = x0
    for _ in range(max_iter):
        fx = x**3 - x - 1
        dfx = 3*x**2 - 1
        x_new = x - fx / dfx
        if abs(x_new - x) < tol:
            return round(x_new, 3)
        x = x_new
    return round(x, 3)

x0 = 1
root = newton_raphson(x0)
print(root)"""


"""def secant_method(x0, x1, tol=0.001, iter=20):
    def f(x):
        return x ** 3 - x - 1

    for i in range(iter):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(x2 - x1) < tol:
            return round(x2, 3)
        x0, x1 = x1, x2
    return round(x2, 3)

x0 = 1
x1 = 1.5
root = secant_method(x0, x1)
print(root)"""


def iteration_method(x0, tol=0.001, iter=20):
    def g(x):
        return (x + 1) ** (1 / 3)

    x = x0
    for i in range(iter):
        x_new = g(x)
        if abs(x_new - x) < tol:
            return round(x_new, 3)
        x = x_new
    return round(x, 3)

x0 = 1
root = iteration_method(x0)
print(root)
