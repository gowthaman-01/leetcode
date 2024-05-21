class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        std::unordered_set<char> set;
        
        // Row
        for (int row = 0; row < 9; row++) {
            set.clear();
            for (int col = 0; col < 9; col++) {
                if (board[row][col] == '.') continue;
                if (set.count(board[row][col])) {
                    return false;
                } else {
                    set.insert(board[row][col]);
                }
            }
        }
        
        // Column
        for (int col = 0; col < 9; col++) {
            set.clear();
            for (int row = 0; row < 9; row++) {
                if (board[row][col] == '.') continue;
                if (set.count(board[row][col])) {
                    return false;
                } else {
                    set.insert(board[row][col]);
                }
            }
        }
        
        // Square
        for (int i = 0; i < 9; i += 3) {
            for (int j = 0; j < 9; j += 3) {
                set.clear();
                for (int row = i; row < i + 3; row++) {
                    for (int col = j; col < j + 3; col++) {
                        if (board[row][col] == '.') continue;
                        if (set.count(board[row][col])) {
                            return false;
                        } else {
                            set.insert(board[row][col]);
                        }
                    }
                }
            }
        }
        
        return true;
    }
};
