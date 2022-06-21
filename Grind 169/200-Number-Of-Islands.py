# DFS
from collections import deque


class Solution:
    def dfs(self, grid, cell, visited):
        if cell not in visited:
            r, c = cell[0], cell[1]
            if r < len(grid) and r >= 0 and c < len(grid[0]) and c >= 0 and grid[r][c] == "1":
                add = [0, 1, 0, -1, 0]
                visited.add(cell)
                for i in range(4):
                    self.dfs(grid, (r + add[i], c + add[i + 1]), visited)

    def numIslands(self, grid) -> int:
        island, visited = 0, set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited and grid[r][c] == "1":
                    island += 1
                    self.dfs(grid, (r, c), visited)
        return island

# BFS


def numIslands(grid):
    island, visited, q = 0, set(), deque([])
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in visited and grid[i][j] == "1":
                island += 1
                q.append((i, j))
                while q:
                    top = q.popleft()
                    r, c = top[0], top[1]
                    if (r, c) not in visited and r < len(grid) and r >= 0 and c < len(grid[0]) and c >= 0 and grid[r][c] == "1":
                        visited.add((r, c))
                        add = [0, 1, 0, -1, 0]
                        for k in range(4):
                            q.append((r + add[k], c + add[k + 1]))
    return island
