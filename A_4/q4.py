def rotate_sort(matrix):
    n = len(matrix)
    
    flat_matrix = [element for row in matrix for element in row]
    
    flat_matrix.sort()
    
    sorted_matrix = [flat_matrix[i * n:(i + 1) * n] for i in range(n)]
    
    rotated_matrix = [[sorted_matrix[n - 1 - i][n - 1 - j] for j in range(n)] for i in range(n)]
    
    return rotated_matrix

matrix = [
    [5, 3, 8],
    [4, 1, 6],
    [7, 2, 9]
]

rotated_sorted_matrix = rotate_sort(matrix)
for row in rotated_sorted_matrix:
    print(row)
