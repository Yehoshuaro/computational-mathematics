import numpy as np

def gauss_seidel(a, b, tol=1e-4, max_iterations=100):
    n = len(b)
    x = np.zeros(n)
    y = np.zeros(n)
    itr = 0

    while itr < max_iterations:
        itr += 1
        for i in range(n):
            x[i] = b[i]
            for j in range(n):
                if i != j:
                    x[i] -= a[i][j] * x[j]
            x[i] /= a[i][i]

        if all(abs(x[i] - y[i]) < tol for i in range(n)):
            break

        y = np.copy(x)

    return x

a = np.array([
    [3, -5, 47, 20],
    [11, 16, 17, 10],
    [56, 22, 11, -18],
    [17, 66, -12, 7]
], dtype=float)

b = np.array([18, 26, 34, 82], dtype=float)

result = gauss_seidel(a, b)
print("Gauss-Seidel result:", result)
