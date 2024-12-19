def newton_raphson(x):
    print("Newton-Raphson Method:")
    for i in range(1, 6):
        fx = x ** 3 - x - 1
        dfx = 3 * x ** 2 - 1
        x = x - fx / dfx
        print("Iteration", i, ":", round(x, 6))
    return round(x, 6)

def secant_method(x0, x1):
    print("\nSecant Method:")
    for i in range(1, 6):
        f_x0 = x0 ** 3 - x0 - 1
        f_x1 = x1 ** 3 - x1 - 1
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        print("Iteration", i, ":", round(x2, 6))
        x0 = x1
        x1 = x2
    return round(x2, 6)

def iteration_method(x):
    print("\nIteration Method:")
    for i in range(1, 6):
        x_new = (x + 1) ** (1 / 3)
        print("Iteration", i, ":", round(x_new, 6))
        x = x_new
    return round(x, 6)

result1 = newton_raphson(1)
result2 = secant_method(1, 1.5)
result3 = iteration_method(1)

print("\nFinal Results:")
print("Newton-Raphson:", result1)
print("Secant Method:", result2)
print("Iteration Method:", result3)
