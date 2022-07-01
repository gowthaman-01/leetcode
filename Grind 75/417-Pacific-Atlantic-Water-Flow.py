class Solution:
    def dfs(self, cell, heights, visited, ocean, canOcean):
        if cell not in visited:
            visited.add(cell)
            r, c = cell[0], cell[1]
            add = [0, 1, 0, -1, 0]
            for i in range(4):
                nr, nc = r + add[i], c + add[i + 1]
                if nr < len(heights) and nr >= 0 and nc < len(heights[0]) and nc >= 0 and heights[nr][nc] >= heights[r][c]:
                    canOcean.add((nr, nc))
                    self.dfs((nr, nc), heights, visited, ocean, canOcean)

                    
    def pacificAtlantic(self, heights):
        res, pacific, atlantic, canPacific, canAtlantic = [], set(), set(), set(), set()
        if not heights: return res
        
        for i in range(len(heights)):
            pacific.add((i, 0))
            atlantic.add((i, len(heights[0]) - 1))
        
        for j in range(len(heights[0])):
            pacific.add((0, j))
            atlantic.add((len(heights) - 1, j))
        
        for cell in pacific:
            visited = set()
            canPacific.add(cell)
            self.dfs(cell, heights, visited, pacific, canPacific)
            
        for cell in atlantic:
            visited = set()
            canAtlantic.add(cell)
            self.dfs(cell, heights, visited, atlantic, canAtlantic)
        
        for possible in canPacific:
            if possible in canAtlantic:
                res.append(possible)
                
        return res