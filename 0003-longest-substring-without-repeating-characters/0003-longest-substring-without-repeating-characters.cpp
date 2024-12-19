class Solution {
public:
    int lengthOfLongestSubstring(const string& s) {
        std::unordered_set<char> unique_chars;
        int longest = 0, l = 0, r = 0;

        while (r < s.length()) {
            if (!unique_chars.count(s[r])) {
                unique_chars.insert(s[r]);
                longest = std::max(longest, r - l + 1);
            } else {
                while (l < r && s[l] != s[r]) {
                    unique_chars.erase(s[l]);
                    l++;

                }
                l++;
            }
            r++;
        }

        return longest;
    }
};