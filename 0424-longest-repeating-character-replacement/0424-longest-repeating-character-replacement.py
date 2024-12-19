class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        l, max_length, max_freq = 0, 0, 0

        for r in range(len(s)):
            count[ord(s[r]) - ord('A')] += 1
            max_freq = max(max_freq, count[ord(s[r]) - ord('A')])

            while r - l + 1 - max_freq > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            max_length = max(max_length, r - l + 1)
        
        return max_length