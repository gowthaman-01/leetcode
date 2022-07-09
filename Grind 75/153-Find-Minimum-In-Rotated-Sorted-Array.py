class Solution:
    def findMin(self, nums):
        res = nums[0]
        l, r = 0, len(nums) - 1
        while nums[l] > nums[r] and l < r:
            m = (l + r) // 2
            if nums[m] > nums[l] and nums[r] > nums[m + 1]:
                return min(res, nums[l], nums[m + 1])
            else:
                if nums[m] > nums[l]:
                    res = min(nums[l], res)
                    l = m + 1
                else:
                    res = min(nums[m + 1], res)
                    r =  m
        
        return min(res, nums[l])