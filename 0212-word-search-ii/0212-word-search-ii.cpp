struct TrieNode {
    std::array<std::unique_ptr<TrieNode>, 26> trie_nodes = {nullptr};
    std::string word = "";
};

class Solution {
private: 
    std::unique_ptr<TrieNode> root = std::make_unique<TrieNode>();

    void construct_trie(std::vector<string>& words) {
        for (std::string& word: words) {
            TrieNode* node = root.get();
            for (char c: word) {
                if (!node->trie_nodes[c - 'a']) {
                    node->trie_nodes[c - 'a'] = std::make_unique<TrieNode>();
                } 
                node = node->trie_nodes[c - 'a'].get();
            }

            node->word = word;
        }
    }

    void dfs(
        std::vector<std::vector<char>>& board, 
        TrieNode* trie, 
        int r, 
        int c,
        std::vector<std::string>& found_words
    ) {
        if (board[r][c] == '-') {
            return;
        }

        if (!trie->word.empty()) {
            found_words.emplace_back(trie->word);
            trie->word = "";
        }

        char temp = board[r][c];
        board[r][c] = '-';

        std::array<int, 5> directions = {0, 1, 0, -1, 0};
        for (int i = 0; i < 4; i++) {
            int nr = r + directions[i];
            int nc = c + directions[i + 1];
            if (nr >=0 && nr < board.size() && nc >= 0 && nc < board[0].size()) {
                if (board[nr][nc] >= 'a' && board[nr][nc] <= 'z' && trie->trie_nodes[board[nr][nc] - 'a']) {
                    dfs(board, trie->trie_nodes[board[nr][nc] - 'a'].get(), nr, nc, found_words);
                }
            }
        }

        board[r][c] = temp;
    }
    


public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        construct_trie(words);

        std::vector<std::string> found_words;
        TrieNode* node = root.get();

        for (int r = 0; r < board.size(); r++) {
            for (int c = 0; c < board[0].size(); c++) {
                if (node->trie_nodes[board[r][c] - 'a']) {
                    dfs(board, node->trie_nodes[board[r][c] - 'a'].get(), r, c, found_words);
                }
            }
        }

        return found_words;    
    }
};