def searchMatrix(matrix, target):
    r, c = len(matrix), len(matrix[0])
    if target < matrix[0][0] or target > matrix[r - 1][c - 1]:
        return False
    # Find row
    left, right = 0, r - 1
    while left <= right:
        m = (right - left) // 2 + left
        if matrix[m][0] > target:
            right = m - 1
        elif matrix[m][0] < target:
            row = m
            left = m + 1
        else:
            return True

    # Find col
    row = matrix[row]
    left, right = 0, c - 1
    while left <= right:
        m = (right - left) // 2 + left
        if target < row[m]:
            right = m - 1
        elif target > row[m]:
            left = m + 1
        else:
            return True
    return False
