class Solution {
private:
    const std::array<int, 5> directions = {0, 1, 0, -1, 0};

    void dfs(int r, int c, std::vector<std::vector<int>>& heights, std::vector<std::vector<int>>& ocean) {
        if (ocean[r][c]) {
            return;
        }
        ocean[r][c] = true;

        for (int i = 0; i < 4; i++) {
            int nr = r + directions[i];
            int nc = c + directions[i + 1];
            if (nr >= 0 && nc >= 0 && nr < heights.size() && nc < heights[0].size() 
                    && heights[nr][nc] >= heights[r][c]) {
                        dfs(nr, nc, heights, ocean);
                } 
        }
    }

public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int ROWS = heights.size(); int COLS = heights[0].size();
        std::vector<std::vector<int>> pacific(ROWS, std::vector<int>(COLS, false));
        std::vector<std::vector<int>> atlantic(ROWS, std::vector<int>(COLS, false));

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (r == 0 || c == 0) {
                    dfs(r, c, heights, pacific);
                }

                if (r == ROWS - 1 || c == COLS - 1) {
                    dfs(r, c, heights, atlantic);
                }
            }
        }

        std::vector<std::vector<int>> result;
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (pacific[r][c] && atlantic[r][c]) {
                    result.push_back({r, c});
                }
            }
        }

        return result;
    }
};