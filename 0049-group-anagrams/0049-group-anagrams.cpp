class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::string, std::vector<std::string>> keyToAnagrams;
        
        for (const std::string &str: strs) {
            keyToAnagrams[getKey(str)].push_back(str);
        }
        
        std::vector<std::vector<std::string>> groupAnagramsList;
        for (auto &p: keyToAnagrams) {
            groupAnagramsList.push_back(std::move(p.second));
        }
        
        return groupAnagramsList;
    }
    
    std::string getKey(string anagram) {
        std::vector<int> alphabetCount(26, 0);
        std::string key = "";
        
        for (char c: anagram) {
            alphabetCount[c - 'a'] += 1;
        }
        for (int count: alphabetCount) {
            key += std::to_string(count) + ',';
        }
        
        return key;
    }
};
