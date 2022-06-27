def missingNumber(nums):
    return sum([i for i in range(0, len(nums) + 1)]) - sum(nums)
