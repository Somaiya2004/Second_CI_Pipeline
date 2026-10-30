"""Program 39: Transpose a matrix."""
def transpose_matrix(matrix):
    if not matrix or not matrix[0]: return []
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
