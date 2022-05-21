def lengthOfLongestSubstring(s):
    h = {}
    l, output = 0, 0
    for r in range(len(s)):
        while s[r] in h:
            h.pop(s[l])
            l += 1
        h[s[r]] = r
        output = max(output, r - l + 1)
    return output
