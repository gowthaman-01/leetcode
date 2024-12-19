class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        std::array<int, 26> count = {0};
        for (int i = 0; i < s.length(); i++) {
            count[s[i] - 'a'] += 1;
            count[t[i] - 'a'] -= 1;
        }

        for (int c: count) {
            if (c) return false;
        }

        return true;
    }
};