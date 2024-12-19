class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_map, t_map = {}, {}
        for c in t:
            t_map[c] = t_map.get(c, 0) + 1
        
        cur, needed = 0, len(t_map)
        l, start = 0, 0
        min_length = len(s) + 1

        for r in range(len(s)):
            if s[r] not in t_map:
                continue
            
            s_map[s[r]] = s_map.get(s[r], 0) + 1
            if (s_map[s[r]] == t_map[s[r]]):
                cur += 1
                while cur == needed:
                    if r - l + 1 < min_length:
                        min_length = r - l + 1
                        start = l
                    
                    if s[l] in t_map:
                        s_map[s[l]] -= 1
                        if s_map[s[l]] < t_map[s[l]]:
                            cur -= 1
                    
                    l += 1
        
        return s[start: start + min_length] if min_length <= len(s) else ""