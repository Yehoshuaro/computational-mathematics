import numpy as np

A = np.array([[50, 107, 36],
              [35, 54, 20],
              [31, 66, 21]])

n = A.shape[0]
L = np.eye(n)
U = A.copy()

for i in range(n):
    for j in range(i+1, n):
        factor = U[j, i] / U[i, i]
        L[j, i] = factor
        U[j] = U[j] - factor * U[i]

L_inv = np.eye(n)
for i in range(n):
    for j in range(i):
        L_inv[i] -= L[i, j] * L_inv[j]

U_inv = np.eye(n)
for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        U_inv[i] -= U[i, j] * U_inv[j]
    U_inv[i] /= U[i, i]

A_inv = U_inv @ L_inv
print(A_inv)
