class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}
        for c in s: 
            count[c] = count.get(c, 0) + 1
            
        freq = [[] for i in range(len(s))]
        for c in count:
            freq[count[c] - 1].append(c)
            
        res = ""
        for i in range(len(s) - 1, -1, -1):
            for c in freq[i]:
                res += c * (i + 1)
                
        return res;