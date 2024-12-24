class Solution {
public:
    bool dfs(std::vector<std::vector<char>>& board, const std::string& word, int r, int c, int cur) {
        if (r < 0 || r >= board.size() || c < 0 || c >= board[0].size() || board[r][c] != word[cur]) {
            return false;
        }
        if (cur == word.size() - 1) return true;
        
        char temp = board[r][c];
        board[r][c] = '-';

        std::array<int, 5> directions = {0, 1, 0, -1, 0};
        for (int i = 0; i < 4; i++) {
            int nr = r + directions[i], nc = c + directions[i + 1];
            if (dfs(board, word, nr, nc, cur + 1)) {
                return true;
            }
    
        }

        board[r][c] = temp;
        return false;
    }

    bool exist(vector<vector<char>>& board, string word) {
        for (int r = 0; r < board.size(); r++) {
            for (int c = 0; c < board[0].size(); c++) {
                if (board[r][c] == word[0]) {
                    if (dfs(board, word, r, c, 0)) {
                        return true;
                    }
                }
            }
        }

        return false;
    }
};