struct TrieNode {
    std::array<std::unique_ptr<TrieNode>, 26> char_arr{nullptr};
    bool is_word = false;
};

class WordDictionary {
private:
    std::unique_ptr<TrieNode> root{nullptr};
public:
    WordDictionary() {
        root = std::make_unique<TrieNode>();
    }
    
    void addWord(string word) {
        TrieNode* node = root.get();

        for (char c: word) {
            if (!node->char_arr[c - 'a']) {
                node->char_arr[c - 'a'] = std::make_unique<TrieNode>();
            }
            node = node->char_arr[c - 'a'].get();
        }

        node->is_word = true;
    }
    
    bool search(string word) {
        return searchHelper(word, 0, root.get());
    }

    bool searchHelper(std::string& word, int pos, TrieNode* node) {
        if (pos == word.size()) {
            return node->is_word;
        } 

        char c = word[pos++];
        if (c != '.') {
            if (!node->char_arr[c - 'a']) {
                return false;
            }

            node = node->char_arr[c - 'a'].get();
            return searchHelper(word, pos, node);
        }

        for (auto& trie_node: node->char_arr) {
            if (trie_node && searchHelper(word, pos, trie_node.get())) {
                return true;
            }
        }

        return false;
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */