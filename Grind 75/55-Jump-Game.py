class Solution:
    def canJump(self, nums):
        nearest, pos = len(nums) - 1, len(nums) - 1
        while pos >= 0:
            if pos + nums[pos] >= nearest: 
                nearest = pos
            pos -= 1
        return True if nearest == 0 else False
        