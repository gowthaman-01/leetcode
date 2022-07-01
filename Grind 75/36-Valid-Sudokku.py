class Solution:
    def getBox(self, r, c):
        if r in {0, 1, 2}:
            if c in {0, 1, 2}:
                return 0
            elif c in {3, 4, 5}:
                return 1
            return 2
        elif r in {3, 4, 5}:
            if c in {0, 1, 2}:
                return 3
            elif c in {3, 4, 5}:
                return 4
            return 5
        else:
            if c in {0, 1, 2}:
                return 6
            elif c in {3, 4, 5}:
                return 7
            return 8
        
    def isValidSudoku(self, board):
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        box = [set() for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    if val in row[i]:
                        return False
                    row[i].add(val)
                    
                    if val in col[j]:
                        return False
                    col[j].add(val)
                    
                    curBox = self.getBox(i, j)
                    if val in box[curBox]:
                        return False
                    box[curBox].add(val)
        return True
                    