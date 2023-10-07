class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> map; 
        for (char c: magazine) {
            map[c]++;
        }
        for (char c: ransomNote) {
            if (!map.count(c)) {
                return false;
            }
            map[c]--;
            if (!map[c]) {
                map.erase(c);
            }
        }
        return true;
    }
};