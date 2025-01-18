class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        for (int r = 0; r < grid.size(); r++) {
            for (int c = 0; c < grid[0].size(); c++) {
                if (r == 0 && c == 0) {
                    continue;
                }

                int left = c > 0 ? grid[r][c - 1] : INT_MAX;
                int up = r > 0 ? grid[r - 1][c] : INT_MAX;

                grid[r][c] += std::min(left, up);
            }
        }

        return grid[grid.size() - 1][grid[0].size() - 1];
    }
};
