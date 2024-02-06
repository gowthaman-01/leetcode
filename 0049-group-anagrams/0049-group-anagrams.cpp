class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map; 
        vector<vector<string>> res; 
        
        for (string s: strs) {
            vector<int> count(26, 0); 
            string key = "";
            for (char c: s) {
                count[c - 'a']++;
            }
            for (int n: count) {
                key += to_string(n) + ",";
            }
            if (map.count(key)) {
                map[key].push_back(s);
            } else {
                map[key] = {s};
            }
        }
        
        for (pair<string, vector<string>> p: map) {
            res.push_back(p.second);
        }
        return res;
    }
};