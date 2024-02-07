class Solution {
public:
    string frequencySort(string s) {
        vector<vector<char>> freq(s.size());
        unordered_map<char, int> count; 
        string res;
        res.reserve(s.size());
        for (char c: s) {
            count[c]++;
        }
        for (auto &p: count) {
            freq[p.second - 1].push_back(p.first);
        }
        for (int i = s.size() - 1; i >= 0; i--) {
            for (char c: freq[i]) {
                res.append(i + 1, c);
            }
        }
        return res;
    }
};