class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }
        unordered_map<char, int> charMap; 
        for (char c: s) {
            charMap[c]++;
        }
        for (char c: t) {
            if (!charMap.count(c) || charMap[c] == 0) {
                return false;
            } else {
                charMap[c]--;
            }
        }
        return true;
    }
};
