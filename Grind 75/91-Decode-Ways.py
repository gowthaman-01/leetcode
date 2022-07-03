class Solution:
    def helper(self, s, cache):
        if not s or (len(s) == 1 and s != "0"): return 1
        if s[0] == "0": return 0
        if s in cache: return cache[s]
        res = 1 * self.helper(s[1:], cache)
        if int(s[0:2]) <= 26:
            res += 1 * self.helper(s[2:], cache)
        cache[s] = res
        return res
    
    def numDecodings(self, s: str) -> int:
        cache = {}
        return self.helper(s, cache)