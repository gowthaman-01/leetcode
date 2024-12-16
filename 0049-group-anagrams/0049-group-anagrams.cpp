class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<string, vector<string>> anagrams_map;

        for (const std::string& str: strs) {
            int count[26] = {0};
            for (char c: str) {
                count[c - 'a']++;
            }

            std::string key = "";
            for (int i = 0; i < 26; i++) {
                key += std::to_string(count[i]) + ".";
            }

            anagrams_map[key].push_back(str);
        }

        std::vector<std::vector<string>> res;
        for (const auto& elem: anagrams_map) {
            res.push_back(std::move(elem.second));
        }

        return res;
    }
};