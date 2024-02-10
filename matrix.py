def validate_matrix(matrix):
    # Check if the matrix is valid: all rows have the same number of elements
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            return False
    return True

def matrix_multiplication(A, B):
    # Validate matrices A and B
    if not validate_matrix(A):
        print('A is an invalid matrix. Number of elements in rows are not equal')
        return
    if not validate_matrix(B):
        print('B is an invalid matrix. Number of elements in rows are not equal')
        return
    
    # Get dimensions of matrices A and B
    m, n = len(A), len(A[0])
    p, q = len(B), len(B[0])
    
    # Check if matrices are compatible for multiplication
    if n != p:
        print('Incompatible matrices for multiplication. Number of columns in A must be equal to the number of rows in B.')
        return
    
    # Perform matrix multiplication
    result = [[0 for _ in range(q)] for _ in range(m)]
    for i in range(m):
        for j in range(q):
            for k in range(p):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

# Sample Input
A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8], [9, 10], [11, 12]]

# Multiply matrices
result = matrix_multiplication(A, B)

# Output the result
if result is not None:
    for row in result:
        print(row)