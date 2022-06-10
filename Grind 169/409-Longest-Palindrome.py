def longestPalindrome(s):
    h = {}
    for c in s:
        h[c] = h.get(c, 0) + 1
    one, two = 0, 0
    for f in h.values():
        two += f // 2
        if f % 2 == 1 and not one:
            one = 1
    return two * 2 + one
