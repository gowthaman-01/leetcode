class Solution {
public:
    int characterReplacement(string s, int k) {
        int l = 0, max_count = 0, max_freq = 0;
        std::array<int, 26> count = {0};
        
        for (int r = 0; r < s.length(); r++) {
            count[s[r] - 'A']++;
            max_freq = std::max(max_freq, count[s[r] - 'A']);
            while (r - l + 1 - max_freq > k) {
                count[s[l] - 'A']--;
                l++;
            }
            max_count = std::max(max_count, r - l + 1);
        }

        return max_count;
    }
};