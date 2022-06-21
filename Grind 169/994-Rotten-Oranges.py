from collections import deque
class Solution:
    def orangesRotting(self, grid):
        visited, fresh, rotten = set(), set(), deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                elif grid[i][j] == 2:
                    rotten.append((i, j))
        time = 0

        while len(fresh) and len(rotten):
            time += 1
            for i in range(len(rotten)):
                top = rotten.popleft()
                r, c = top[0], top[1]    
                if (r, c) not in visited:
                    visited.add((r, c))
                    add = [0, 1, 0, -1, 0]
                    for k in range(4):
                        nr, nc = r + add[k], c + add[k + 1]
                        if (nr, nc) in fresh:
                            fresh.remove((nr, nc))
                            rotten.append((nr, nc))
                                        
                                     
        if len(fresh) == 0:
            return time
        else:
            return -1
                                     
                        