struct TrieNode {
    std::unordered_map<char, std::unique_ptr<TrieNode>> char_map;
    bool is_word = false;
};

class Trie {
private:
    std::unique_ptr<TrieNode> root{nullptr};
public:
    Trie() {
        root = std::make_unique<TrieNode>();
    }
    
    void insert(string word) {
        TrieNode* node = root.get();

        for (char c: word) {
            if (!node->char_map.count(c)) {
                node->char_map[c] = std::make_unique<TrieNode>();
            }
            node = node->char_map[c].get();
        }

        node->is_word = true;
    }
    
    bool search(string word) {
        TrieNode* node = root.get();
        
        for (char c: word) {
            if (!node->char_map.count(c)) {
                return false;
            }
            node = node->char_map[c].get();
        }
        
        return node->is_word;
    }
    
    bool startsWith(string prefix) {
         TrieNode* node = root.get();
        
        for (char c: prefix) {
            if (!node->char_map.count(c)) {
                return false;
            }
            node = node->char_map[c].get();
        }

        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */