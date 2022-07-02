class Solution:
    def subarraySum(self, nums, k):
        h, cur, res = {0: 1}, 0, 0
        for num in nums:
            cur += num  
            if cur - k in h:
                res += h[cur - k]
            h[cur] = h.get(cur, 0) + 1
        return res
