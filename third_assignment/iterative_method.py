import numpy as np

A = np.array([[1, 10, 1],
              [2, 0, 1],
              [3, 3, 2]])

B = np.array([[0.4, 2.4, -1.4],
              [0.14, 0.14, -0.14],
              [-0.85, -3.8, 2.8]])

I = np.eye(3)
R = I - A @ B

A_inv_approx = B
for _ in range(5):
    A_inv_approx = A_inv_approx + R @ A_inv_approx

print(A_inv_approx)
