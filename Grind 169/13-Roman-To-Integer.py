def romanToInt(s):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0
    pos = -1
    prev = None
    for i in range(len(s)):
        current = s[pos]
        if prev == None:
            prev = current
        if d[prev] > d[current]:
            integer -= d[current]
        else:
            integer += d[current]
        prev = current
        pos -= 1
    return integer
                