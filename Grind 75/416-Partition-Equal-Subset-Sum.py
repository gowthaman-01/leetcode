class Solution:
    def helper(self, nums, target, store):
        if target == 0:
            return True
        if target < 0:
            return False
        if target in store:
            return store[target]
        for i in range(len(nums)):
            if self.helper(nums[0: i] + nums[i + 1:], target - nums[i], store):
                return True
        store[target] = False
        return False
    
    def canPartition(self, nums) -> bool:
        target = 0
        for num in nums:
            target += num
        if target % 2 != 0:
            return False
        target /= 2
        store = {}
        return self.helper(nums, target, store)
    