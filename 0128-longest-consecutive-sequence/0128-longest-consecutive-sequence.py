class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        unique_nums = set(nums)

        for num in unique_nums:
            if num - 1 in unique_nums:
                continue
            
            cur_length = 0
            while num in unique_nums:
                num += 1
                cur_length += 1
            
            max_length = max(max_length, cur_length)

        return max_length