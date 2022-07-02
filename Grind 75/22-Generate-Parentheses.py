class Solution:
    def backTrack(self, n, o, c, total):
        if o == c == total:
            return [""]
        res = []
        if o < total:
            after = self.backTrack(n - 1, o + 1, c, total)
            for possible in after:
                new = "("  + possible
                res.append(new)
        if c < total and o > c: 
            after = self.backTrack(n - 1, o, c + 1, total)
            for possible in after:
                new = ")" + possible
                res.append(new)
        return res
        
    def generateParenthesis(self, n):
        return self.backTrack(n, 0, 0, n)