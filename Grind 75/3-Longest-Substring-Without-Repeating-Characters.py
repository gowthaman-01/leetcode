def lengthOfLongestSubstring(s):
    count, repeat, l = 0, set(), 0
    for r in range(len(s)):
        while s[r] in repeat:
            repeat.remove(s[l])
            l += 1
        repeat.add(s[r])
        count = max(count, r - l + 1)
    return count
                