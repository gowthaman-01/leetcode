class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        res = None
        if nums[0] + nums[1] + nums[2] >= target: return nums[0] + nums[1] + nums[2]
        if nums[-1] + nums[-2] + nums[-3] <= target: return nums[-1] + nums[-2] + nums[-3]
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]: continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                add = nums[l] + nums[r] + num
                if add == target:
                    return target
                if add > target:
                    if res == None or abs(add - target) < abs(res - target):
                        res = add
                    r -= 1
                else:
                    if res == None or abs(add - target) < abs(res - target):
                        res = add
                    l += 1
        return res
        
        
