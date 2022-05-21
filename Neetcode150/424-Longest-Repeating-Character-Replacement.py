def characterReplacement(self, s: str, k: int) -> int:
    h = {}
    r, l = 0, 0
    most = 0
    output = 0
    while r < len(s):
        h[s[r]] = h.get(s[r], 0) + 1
        most = max(most, h[s[r]])
        while r - l + 1 - most > k:
            h[s[l]] -= 1
            l += 1
        output = max(r - l + 1, output)
        r += 1
    return output
