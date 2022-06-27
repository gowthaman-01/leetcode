class Solution:
    def dfs(self, cell, board, explored, index, word):
        if index > len(word):
            return False
        if index == len(word):
            return True
        if cell not in explored:
            r, c = cell[0], cell[1]
            add = [0, 1, 0, -1, 0]
            for i in range(4):
                explored.add(cell)
                nr, nc = r + add[i], c + add[i + 1]
                if nr < len(board) and nr >= 0 and nc < len(board[0]) and nc >= 0 and board[nr][nc] == word[index] and (nr, nc) not in explored:
                    if self.dfs((nr, nc), board, explored, index + 1, word):
                        return True
                explored.remove(cell)
        return False
            
    def exist(self, board, word) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    explored = set()
                    possible = self.dfs((i, j), board, explored, 1, word)
                    if possible:
                        return True
        return False
                    