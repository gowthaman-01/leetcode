class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> map; 
        for (char c: s) {
            map[c]++;
        }
        for (char c: t) {
            if (!map.count(c)) {
                return false;
            }
            map[c]--;
            if (!map[c]) {
                map.erase(c);
            }
        }
        return map.empty();
    }
};