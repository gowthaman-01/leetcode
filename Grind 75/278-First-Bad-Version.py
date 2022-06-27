def firstBadVersion(n):
    l, r = 1, n
    first = None
    while l <= r:
        m = l + (r - l) // 2
        if not isBadVersion(m):
            l = m + 1
        else:
            if first == None:
                first = m
            else:
                first = min(m, first)
            r = m - 1
    return first
    