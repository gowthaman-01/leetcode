class Solution {
public:
    string frequencySort(string s) {
        vector<vector<char>> freq(s.size());
        unordered_map<char, int> count; 
        string res = "";
        for (char c: s) {
            count[c]++;
        }
        for (auto &p: count) {
            freq[p.second - 1].push_back(p.first);
        }
        for (int i = s.size() - 1; i >= 0; i--) {
            for (char c: freq[i]) {
                for (int j = 0; j < i + 1; j++) {
                    res += c;
                }
            }
        }
        return res;
    }
};