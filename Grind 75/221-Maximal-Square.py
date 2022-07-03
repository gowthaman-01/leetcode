class Solution:
    def fill(self, matrix, dp, cell, visited):
        r, c = cell[0], cell[1]
        if r >= len(matrix) - 1 or c >= len(matrix[0]) - 1 or (r, c) in visited: return 
        visited.add((r, c))
        
        self.fill(matrix, dp, (r, c + 1), visited)
        self.fill(matrix, dp, (r + 1, c), visited)
        self.fill(matrix, dp, (r + 1, c + 1), visited)
        
        if dp[r][c] == 0: return 
        neighbour = min(dp[r + 1][c], dp[r][c + 1], dp[r + 1][c + 1])
        dp[r][c] = neighbour + 1
        self.res = max(self.res, dp[r][c])
    
    
    
    def maximalSquare(self, matrix):
        self.res = 0
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    self.res = 1
                    dp[i][j] = 1
        visited = set()
        self.fill(matrix, dp, (0, 0), visited)
        return self.res ** 2