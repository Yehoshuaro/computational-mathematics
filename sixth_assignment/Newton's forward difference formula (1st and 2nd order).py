def newton_forward_diff1(y, h):
    delta1 = y[1] - y[0]
    delta2 = y[2] - 2 * y[1] + y[0]
    delta3 = y[3] - 3 * y[2] + 3 * y[1] - y[0]

    f_prime = (delta1 / h) - (delta2 / (2 * h)) + (delta3 / (3 * h))
    return f_prime

x_vals = [0, 1, 2, 3, 4]
y_vals = [1, 2, 4, 8, 16]
h = x_vals[1] - x_vals[0]

result1 = newton_forward_diff1(y_vals, h)
print("First derivative at x=0:", result1)

def newton_forward_diff2(y, h):
    delta2 = y[2] - 2 * y[1] + y[0]
    delta3 = y[3] - 3 * y[2] + 3 * y[1] - y[0]

    f_double_prime = (delta2 / h**2) - (delta3 / h**2)
    return f_double_prime

result2 = newton_forward_diff2(y_vals, h)
print("Second derivative at x=0:", result2)


