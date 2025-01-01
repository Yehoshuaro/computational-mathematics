import numpy as np

matrix = np.array([[1, np.sqrt(2), 2],
                   [np.sqrt(2), 3, np.sqrt(2)],
                   [2, np.sqrt(2), 1]], dtype=float)
matrix_size = len(matrix)
eigenvectors_matrix = np.eye(matrix_size)

for _ in range(100):
    i, j = np.unravel_index(np.argmax(np.abs(np.triu(matrix, 1))), matrix.shape)
    if matrix[i, j] == 0:
        break
    rotation_angle = 0.5 * np.arctan2(2 * matrix[i, j], matrix[j, j] - matrix[i, i])
    cosine = np.cos(rotation_angle)
    sine = np.sin(rotation_angle)
    rotation_matrix = np.eye(matrix_size)
    rotation_matrix[i, i] = rotation_matrix[j, j] = cosine
    rotation_matrix[i, j] = sine
    rotation_matrix[j, i] = -sine
    matrix = rotation_matrix.T @ matrix @ rotation_matrix
    eigenvectors_matrix = eigenvectors_matrix @ rotation_matrix

eigenvalues = np.diag(matrix)
eigenvectors = eigenvectors_matrix

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:")
print(eigenvectors)

