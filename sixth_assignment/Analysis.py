# f(x)=x**2 +2x+1
# f'(x)=2x+2

def euler(f, x0, y0, h, steps):
    x, y = x0, y0
    for _ in range(steps):
        y += h * f(x, y)
        x += h
    return y

def modified_euler(f, x0, y0, h, steps):
    x, y = x0, y0
    for _ in range(steps):
        y_predict = y + h * f(x, y)
        y += (h / 2) * (f(x, y) + f(x + h, y_predict))
        x += h
    return y

def runge_kutta_3(f, x0, y0, h, steps):
    x, y = x0, y0
    for _ in range(steps):
        k1 = f(x, y)
        k2 = f(x + h / 2, y + h * k1 / 2)
        k3 = f(x + h, y - h * k1 + 2 * h * k2)
        y += (h / 6) * (k1 + 4 * k2 + k3)
        x += h
    return y

def runge_kutta_4(f, x0, y0, h, steps):
    x, y = x0, y0
    for _ in range(steps):
        k1 = f(x, y)
        k2 = f(x + h / 2, y + h * k1 / 2)
        k3 = f(x + h / 2, y + h * k2 / 2)
        k4 = f(x + h, y + h * k3)
        y += (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x += h
    return y

def f(x, y):
    return x + y

x0, y0, h, steps = 0, 1, 0.1, 2

y_euler = euler(f, x0, y0, h, steps)
y_mod_euler = modified_euler(f, x0, y0, h, steps)
y_rk3 = runge_kutta_3(f, x0, y0, h, steps)
y_rk4 = runge_kutta_4(f, x0, y0, h, steps)

print(f"Euler: {y_euler}")
print(f"Modified Euler: {y_mod_euler}")
print(f"Runge-Kutta 3rd order: {y_rk3}")
print(f"Runge-Kutta 4th order: {y_rk4}")