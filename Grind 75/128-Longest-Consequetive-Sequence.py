class Solution:
    def longestConsecutive(self, nums):
        long, hashSet = 0, set(nums)
        for num in hashSet:
            if (num - 1) not in hashSet:
                start, cur = num, 0
                while start in hashSet:
                    cur += 1
                    start += 1
                long = max(long, cur)
        return long