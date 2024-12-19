class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = set()
        l, longest = 0, 0

        for r in range(len(s)):
            if s[r] not in unique_chars:
                unique_chars.add(s[r])
                longest = max(longest, r - l + 1)
            else:
                while l < r and s[l] != s[r]:
                    unique_chars.remove(s[l])
                    l += 1
                l += 1
        
        return longest
        
