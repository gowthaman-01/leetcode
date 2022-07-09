class Solution:
    def helper(self, nums, target, store):
        if target in store:
            return store[target]
        if not nums or target < 0: return 0
        if target == 0: return 1
        res = 0
        for i in range(len(nums)):
            res += self.helper(nums, target - nums[i], store)
        store[target] = res
        return store[target]
    def combinationSum4(self, nums, target):
        store = {}
        return self.helper(nums, target, store)
    