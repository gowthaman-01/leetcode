class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_map = {}
        for c in s: 
            char_map[c] = char_map.get(c, 0) + 1
        for c in t: 
            if c not in char_map or char_map[c] == 0: 
                return False
            char_map[c] -= 1
        return True
        