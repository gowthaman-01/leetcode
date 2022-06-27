class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        while nums[slow] != nums[fast]:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]

        new = 0
        while nums[new] != nums[slow]:
            new = nums[new]
            slow = nums[slow]
        return nums[new]
    