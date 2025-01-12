import numpy as np

def relaxation_method(A, b, omega, tol=1e-10, max_iter=1000):
    n = len(b)
    x = np.zeros_like(b, dtype=float)
    for iteration in range(max_iter):
        x_new = np.copy(x)
        for i in range(n):
            sum1 = np.dot(A[i, :i], x_new[:i])
            sum2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (1 - omega) * x[i] + (omega / A[i, i]) * (b[i] - sum1 - sum2)
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, iteration + 1
        x = x_new
    return x, max_iter

# Relaxation Method Explanation
# 1. This method iteratively solves Ax = b using a relaxation factor omega (0 < omega <= 2)
# 2. It updates each variable step by step until the solution converges or max iterations are reached
# 3. The result is the solution vector x and the number of iterations performed