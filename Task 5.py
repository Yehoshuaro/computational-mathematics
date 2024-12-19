def iteration_method_with_error(x_start, tolerance):
    print("Iteration Method with Errors:")
    x_old = x_start
    for i in range(1, 11):
        x_new = (x_old + 1) ** (1 / 3)
        Ea = abs(x_new - x_old)
        Er = abs((x_new - x_old) / x_new)
        print("Iteration", i, ": x =", round(x_new, 6), "| Ea =", round(Ea, 6), "| Er =", round(Er, 6))

        if Ea < tolerance:
            print("Terminating: Absolute error is small enough")
            break
        if Er < tolerance:
            print("Terminating: Relative error is small enough")
            break

        x_old = x_new

x_start = 1
tolerance = 0.000001

iteration_method_with_error(x_start, tolerance)
