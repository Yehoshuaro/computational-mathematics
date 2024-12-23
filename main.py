def cramer_method(matrix, results):
    def determinant(mat):
        if len(mat) == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
        det = 0
        for i in range(len(mat)):
            sub_mat = [row[:i] + row[i + 1:] for row in mat[1:]]
            det += ((-1) ** i) * mat[0][i] * determinant(sub_mat)
        return det

    det_main = determinant(matrix)
    solutions = []
    for i in range(len(matrix)):
        temp_mat = [row[:] for row in matrix]
        for j in range(len(matrix)):
            temp_mat[j][i] = results[j]
        solutions.append(determinant(temp_mat) / det_main)
    return solutions



def gauss_method(matrix, results):
    n = len(matrix)
    for i in range(n):
        divisor = matrix[i][i]
        for j in range(i, n):
            matrix[i][j] /= divisor
        results[i] /= divisor

        for k in range(i + 1, n):
            factor = matrix[k][i]
            for j in range(i, n):
                matrix[k][j] -= factor * matrix[i][j]
            results[k] -= factor * results[i]

    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = results[i]
        for j in range(i + 1, n):
            solution[i] -= matrix[i][j] * solution[j]
    return solution



def jacobi_method(matrix, results, max_iterations=100, tol=1e-6):
    n = len(matrix)
    x = [0] * n
    for _ in range(max_iterations):
        new_x = x[:]
        for i in range(n):
            sum_ax = sum(matrix[i][j] * x[j] for j in range(n) if j != i)
            new_x[i] = (results[i] - sum_ax) / matrix[i][i]
        if all(abs(new_x[i] - x[i]) < tol for i in range(n)):
            break
        x = new_x
    return x



def gauss_seidel_method(matrix, results, max_iterations=100, tol=1e-6):
    n = len(matrix)
    x = [0] * n
    for _ in range(max_iterations):
        new_x = x[:]
        for i in range(n):
            sum_ax = sum(matrix[i][j] * new_x[j] for j in range(n) if j != i)
            new_x[i] = (results[i] - sum_ax) / matrix[i][i]
        if all(abs(new_x[i] - x[i]) < tol for i in range(n)):
            break
        x = new_x
    return x

matrix = [
    [3, -5, 47, 20],
    [11, 16, 17, 10],
    [56, 22, 11, -18],
    [17, 66, -12, 7]
]
results = [18, 26, 34, 82]

solution_cramer = cramer_method([row[:] for row in matrix], results[:])
solution_gauss = gauss_method([row[:] for row in matrix], results[:])
solution_jacobi = jacobi_method([row[:] for row in matrix], results[:])
solution_gauss_seidel = gauss_seidel_method([row[:] for row in matrix], results[:])

print("Cramer:", solution_cramer)
print("Gauss:", solution_gauss)
print("Jacobi:", solution_jacobi)
print("Gauss-Seidel:", solution_gauss_seidel)
