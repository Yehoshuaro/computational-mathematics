import numpy as np

matrix = np.array([[3, -5, 47, 20],
                   [11, 16, 17, 10],
                   [56, 22, 11, -18],
                   [17, 66, -12, 7]], dtype=float)

vector = np.array([18, 26, 34, 82], dtype=float)

def cramer_method(matrix, vector):
    determinant_main = np.linalg.det(matrix)
    if determinant_main == 0:
        return "No solution"

    solutions = []
    for column_index in range(len(matrix)):
        temp_matrix = matrix.copy()
        temp_matrix[:, column_index] = vector
        solutions.append(np.linalg.det(temp_matrix) / determinant_main)
    return solutions

def gaussian_method(matrix, vector):
    num_rows = len(matrix)
    for pivot_row in range(num_rows):
        max_row = np.argmax(abs(matrix[pivot_row:, pivot_row])) + pivot_row
        matrix[[pivot_row, max_row]] = matrix[[max_row, pivot_row]]
        vector[pivot_row], vector[max_row] = vector[max_row], vector[pivot_row]

        for target_row in range(pivot_row + 1, num_rows):
            factor = matrix[target_row][pivot_row] / matrix[pivot_row][pivot_row]
            matrix[target_row, pivot_row:] -= factor * matrix[pivot_row, pivot_row:]
            vector[target_row] -= factor * vector[pivot_row]

    solutions = np.zeros(num_rows)
    for row in range(num_rows - 1, -1, -1):
        solutions[row] = (vector[row] - np.dot(matrix[row, row + 1:], solutions[row + 1:])) / matrix[row, row]
    return solutions

def jacobi_method(matrix, vector, max_iterations=25):
    num_rows = len(matrix)
    solutions = np.zeros(num_rows)
    for _ in range(max_iterations):
        new_solutions = np.copy(solutions)
        for row in range(num_rows):
            sum_terms = sum(matrix[row, col] * solutions[col] for col in range(num_rows) if col != row)
            new_solutions[row] = (vector[row] - sum_terms) / matrix[row, row]
        solutions = new_solutions
    return solutions

def gauss_seidel_method(matrix, vector, max_iterations=25):
    num_rows = len(matrix)
    solutions = np.zeros(num_rows)
    for _ in range(max_iterations):
        for row in range(num_rows):
            sum_terms = sum(matrix[row, col] * solutions[col] for col in range(num_rows) if col != row)
            solutions[row] = (vector[row] - sum_terms) / matrix[row, row]
    return solutions

print("Cramer's Method Solution:", cramer_method(matrix.copy(), vector.copy()))
print("Gaussian Method Solution:", gaussian_method(matrix.copy(), vector.copy()))
print("Jacobi Method Solution:", jacobi_method(matrix.copy(), vector.copy()))
print("Gauss-Seidel Method Solution:", gauss_seidel_method(matrix.copy(), vector.copy()))