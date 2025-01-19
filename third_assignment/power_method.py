import numpy as np

matrix = np.array([[2, -1, 0],
                   [-1, 2, -1],
                   [0, -1, 2]])

current_vector = np.array([1, 0, 0], dtype=float)
for _ in range(10):
    next_vector = np.dot(matrix, current_vector)
    current_vector = next_vector / np.linalg.norm(next_vector)
largest_eigenvalue = np.dot(current_vector, np.dot(matrix, current_vector)) / np.dot(current_vector, current_vector)

print("Largest eigenvalue:", largest_eigenvalue)
print("Corresponding eigenvector:", current_vector)
