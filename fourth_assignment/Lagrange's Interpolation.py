x_points = [1, 2, 3, 4]
y_points = [1, 5, 11, 8]

def lagrange_interpolation(x_values, y_values, target):
    n = len(x_values)
    interpolation_sum = 0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (target - x_values[j]) / (x_values[i] - x_values[j])
        interpolation_sum += term

    return interpolation_sum


y_at_1_5 = lagrange_interpolation(x_points, y_points, 1.5)

print(f"y(1.5) = {y_at_1_5:.3f}")


# Lagrange Interpolation Formula:
# y(target) = summation (y_i * pi ((target - x_j) / (x_i - x_j))), for i != j
