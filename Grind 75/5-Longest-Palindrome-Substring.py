def longestPalindrome(s):
    output = ""
    if not s:
        return output
    for i in range(len(s)):
        r, l = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > len(output):
                output = s[l: r + 1]
            r += 1
            l -= 1
        r, l = i + 1, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > len(output):
                output = s[l: r + 1]
            r += 1
            l -= 1
    return output
        