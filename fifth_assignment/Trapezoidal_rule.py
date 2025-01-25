def trapezoidal_rule(lower_limit, upper_limit, sub_intervals, function):
    step_size = (upper_limit - lower_limit) / sub_intervals
    total_area = 0.5 * (function(lower_limit) + function(upper_limit))

    for i in range(1, sub_intervals):
        x = lower_limit + i * step_size
        total_area += function(x)

    return total_area * step_size

def cubic_function(x):
    return x**3

lower_limit = 0
upper_limit = 1
sub_intervals = 5

result = trapezoidal_rule(lower_limit, upper_limit, sub_intervals, cubic_function)
print(result)
