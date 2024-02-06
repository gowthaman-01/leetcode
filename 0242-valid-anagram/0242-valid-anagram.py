class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = {}
        for c in s: 
            h[c] = h.get(c, 0) + 1
        for c in t: 
            if c not in h: 
                return False
            h[c] -= 1
            if not h[c]: 
                h.pop(c)
        return not bool(h)
        