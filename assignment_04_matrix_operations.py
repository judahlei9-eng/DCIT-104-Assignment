# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
def read_matrix(rows, cols, label=""):
    print(f"Enter {label} matrix:")
    matrix = []
    for i in range(rows):
        row_values = input(f"Enter row {i + 1}: ").split()
        row = [float(value) for value in row_values]
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        formatted_row = "  ".join(f"{value:g}" for value in row)
        print(formatted_row)
    print()


def transpose_matrix(matrix, rows, cols):
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result


def add_matrices(matrix_a, matrix_b, rows, cols):
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
    return result


def multiply_matrices(matrix_a, matrix_b, m, n, p):
    result = [[0 for _ in range(p)] for _ in range(m)]
    for i in range(m):
        for j in range(p):
            total = 0
            for k in range(n):
                total += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = total
    return result


if __name__ == "__main__":
    # ---------------- PART A: Transpose ----------------
    print("=== PART A: Transpose a Matrix ===")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, cols)

    print("\nOriginal Matrix:")
    print_matrix(matrix)

    transposed = transpose_matrix(matrix, rows, cols)
    print("Transposed Matrix:")
    print_matrix(transposed)

    # ---------------- PART B: Addition ----------------
    print("=== PART B: Add Two Matrices ===")
    add_rows = int(input("Enter number of rows for both matrices: "))
    add_cols = int(input("Enter number of columns for both matrices: "))

    matrix_a = read_matrix(add_rows, add_cols, label="first")
    matrix_b = read_matrix(add_rows, add_cols, label="second")

    sum_matrix = add_matrices(matrix_a, matrix_b, add_rows, add_cols)
    print("\nSum Matrix:")
    print_matrix(sum_matrix)

    # ---------------- PART C: Multiplication ----------------
    print("=== PART C: Multiply Two Matrices ===")
    m = int(input("Enter rows of Matrix A: "))
    n = int(input("Enter columns of Matrix A (= rows of Matrix B): "))
    p = int(input("Enter columns of Matrix B: "))

    matrix_a = read_matrix(m, n, label="A")
    matrix_b = read_matrix(n, p, label="B")

    product_matrix = multiply_matrices(matrix_a, matrix_b, m, n, p)
    print("\nProduct Matrix (A x B):")
    print_matrix(product_matrix)
# =============================================================================

