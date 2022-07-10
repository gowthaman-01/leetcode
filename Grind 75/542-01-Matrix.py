from collections import deque
class Solution:
    def updateMatrix(self, mat):
        q, dist = deque([]), 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i, j))
                if mat[i][j] == 1:
                    mat[i][j] = -1
        while q:
            for i in range(len(q)):
                top = q.popleft()
                r, c = top[0], top[1]
                if mat[r][c] == -1:
                    mat[r][c] = dist
                add = [0, 1, 0, -1, 0]
                for j in range(4):
                    nr, nc = r + add[j], c + add[j + 1]
                    if nr >= 0 and nr < len(mat) and nc >= 0 and nc < len(mat[0]) and mat[nr][nc] == -1:
                        q.append((nr, nc))
            dist += 1
        return mat

    