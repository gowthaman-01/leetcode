class Solution {
public:
    bool isEqual(char c1, char c2) {
        if (std::isdigit(c1) && std::isdigit(c2)) {
            return c1 == c2;
        } else if (std::isdigit(c1) || std::isdigit(c2)) {
            return false;
        } else {
            return std::tolower(c1) == std::tolower(c2);
        }
    }
    bool isPalindrome(string s) {
        int l = 0; int r = s.length() - 1;
        while (l <= r) {
            while (l < r && !std::isalnum(s[l])) {
                l++;
            }
            while (l < r && !std::isalnum(s[r])) {
                r--;
            }
            if (!isEqual(s[l], s[r])) {
                return false;
            }
            l++;
            r--;
        }

        return true;
    }
};