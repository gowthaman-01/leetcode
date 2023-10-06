class Solution {
public:
    void dfs(vector<vector<int>>& image, int sr, int sc, int original, int color, vector<vector<bool>>& visited) {
        if (visited[sr][sc]) {
            return;
        }
        image[sr][sc] = color;
        visited[sr][sc] = true;
        vector<int> add({0, 1, 0, -1, 0});
        for (int i = 0; i < 4; i++) {
            int nr = sr + add[i];
            int nc = sc + add[i + 1];
            if (nr < image.size() && nc < image[0].size() && nr >= 0 && nc >= 0 && image[nr][nc] == original) {
                dfs(image, nr, nc, original, color, visited);
            }
        }
    }

    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        if (image[sr][sc] == color) {
            return image;
        } 
        vector<vector<bool>> visited(image.size(), vector<bool>(image[0].size(), false));
        dfs(image, sr, sc, image[sr][sc], color, visited);
        return image;
    }
};