class Solution {
private:
    void dfs(std::vector<std::vector<char>>& grid, int r, int c) {
        grid[r][c] = '-';
        
        static const std::array<int, 5> directions = {0, 1, 0, -1, 0};
        for (int i = 0; i < 4; i++) {

            int nr = r + directions[i];
            int nc = c + directions[i + 1];
            if (nr >= 0 && nr < grid.size() && nc >= 0 && nc < grid[0].size() && grid[nr][nc] == '1') {
                dfs(grid, nr, nc);
            }
        }
    }

public:
    int numIslands(vector<vector<char>>& grid) {
        int island_count = 0;

        for (int r = 0; r < grid.size(); r++) {
            for (int c = 0; c < grid[0].size(); c++) {
                if (grid[r][c] == '1') {
                    island_count++;
                    dfs(grid, r, c);
                }
            }
        }

        return island_count;
    }
};