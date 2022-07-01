class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h, r, l, most, res = {}, 0, 0, 0, 0
        while r < len(s):
            h[s[r]] = h.get(s[r], 0) + 1
            most = max(most, h[s[r]])
            while r - l + 1 - most > k:
                h[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res