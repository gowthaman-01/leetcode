class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        
        for i, num in enumerate(nums):
            if (complement := target - num) in num_to_index:
                return [i, num_to_index[complement]]
            num_to_index[num] = i

        return []