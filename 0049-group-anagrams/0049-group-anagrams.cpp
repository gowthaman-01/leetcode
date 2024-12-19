class Solution {
public:
    std::string key_from_string(const std::string& str) {
        std::array<int, 26> char_count = {0};
        for (char c: str) {
            char_count[c - 'a']++;
        }

        std::string key = "";
        for (int count: char_count) {
            key += std::to_string(count) + "/";
        }

        return key;
    }

    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::string, std::vector<std::string>> anagrams;

        for (const std::string& str: strs) {
            anagrams[key_from_string(str)].push_back(str);
        }

        std::vector<std::vector<std::string>> res;
        for (const auto& elem: anagrams) {
            res.push_back(elem.second);
        }

        return res;
    }
};