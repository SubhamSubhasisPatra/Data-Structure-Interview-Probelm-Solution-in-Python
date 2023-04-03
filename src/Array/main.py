def set_matrix_zero(matrix) -> None:
    """
    :description: Sets the matrix with zero values non optimized
    :param matrix:
    :return: None
    """
    row_set, col_set = set(), set()

    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            if matrix[row][col] == 0:
                row_set.add(row)
                col_set.add(col)

    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            if col in col_set:
                matrix[row][col] = 0
            if row in row_set:
                matrix[row][col] = 0
    print(matrix)


if __name__ == '__main__':
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    set_matrix_zero(matrix)
