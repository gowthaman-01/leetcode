class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            num2 = target - num
            if num2 in h: 
                return [i, h[num2]]
            h[num] = i
        