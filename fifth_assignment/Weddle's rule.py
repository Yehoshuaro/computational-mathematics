a = 0
b = 1
n = 6

def weddles_rule(a, b, f, n):
    if n % 6 != 0:
        raise ValueError("Number of intervals must be a multiple of 6")

    h = (b - a) / n
    x_values = [a + i * h for i in range(n + 1)]
    y_values = [f(x) for x in x_values]

    integral = 0
    for i in range(0, n, 6):
        integral += (3 * h / 10) * (y_values[i] + 5 * y_values[i + 1] + y_values[i + 2]
            + 6 * y_values[i + 3] + y_values[i + 4] + 5 * y_values[i + 5] + y_values[i + 6])
    return integral

def function(x):
    return 1 / (1 + x**2)

try:
    result = weddles_rule(a, b, function, n)
    print("Approximated integral:", result)
except ValueError as e:
    print(e)
