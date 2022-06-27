def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    sh, th = {}, {}
    for i in range(len(s)):
        sh[s[i]] = sh.get(s[i], 0) + 1
        th[t[i]] = th.get(t[i], 0) + 1
    for c in sh.keys():
        if sh[c] != th.get(c, 0):
            return False
    return True
