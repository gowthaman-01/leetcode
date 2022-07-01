class Solution:
    def findMaxLength(self, nums):
        count, hmap, res = 0, {}, 0
        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1
            if count == 0:
                res = max(res, i + 1)
            if count in hmap:
                res = max(res, i - hmap[count])
            else:
                hmap[count] = i
        return res