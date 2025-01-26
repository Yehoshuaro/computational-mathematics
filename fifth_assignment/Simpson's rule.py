def simpsons_second_rule(a, b, f, n):
    if n % 3 != 0:
        raise ValueError("Number of intervals must be a multiple of 3")

    h = (b - a) / n
    x_values = [a + i * h for i in range(n + 1)]
    y_values = [f(x) for x in x_values]

    integral = (3 * h / 8) * (
            y_values[0]+ 3 * sum(y_values[i] for i in range(1, n, 3))
            + 3 * sum(y_values[i] for i in range(2, n, 3))
            + 2 * sum(y_values[i] for i in range(3, n, 3))
            + y_values[-1]
    )
    return integral

def function(x):
    return 1 / (1 + x ** 3)

a = 0
b = 9
n = 3

try:
    result = simpsons_second_rule(a, b, function, n)
    print("Approximated integral:", result)
except ValueError as e:
    print(e)
