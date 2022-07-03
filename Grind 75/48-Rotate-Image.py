class Solution:
    def helper(self, matrix, l, r):
        if r - l <= 0: return 
        for i in range(r - l):
            temp1 = matrix[l + i][r]
            matrix[l + i][r] = matrix[l][l + i]
            temp2 = matrix[r][r - i]
            matrix[r][r - i] = temp1
            temp1 = matrix[r - i][l]
            matrix[r - i][l] = temp2 
            matrix[l][l + i] = temp1
        self.helper(matrix, l + 1, r - 1)
        
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.helper(matrix, 0, len(matrix) - 1)