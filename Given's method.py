import numpy as np

def givens_rotation(A):
    rows, cols = A.shape
    Q = np.eye(rows)
    R = A.copy()

    for j in range(cols):
        for i in range(rows - 1, j, -1):
            if R[i, j] != 0:
                r = np.hypot(R[i - 1, j], R[i, j])
                c = R[i - 1, j] / r
                s = -R[i, j] / r

                G = np.eye(rows)
                G[i - 1, i - 1] = c
                G[i, i] = c
                G[i - 1, i] = -s
                G[i, i - 1] = s

                R = G @ R
                Q = Q @ G.T

    return Q, R

# Givens Rotation Method Explanation in my understanding
# 1. This method removes specific elements below the diagonal in a matrix
# 2. It uses rotation matrices to zero out these elements step by step
# 3. The output is two matrices: Q (orthogonal) and R (upper triangular)
