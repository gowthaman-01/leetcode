def maxProduct(self, nums: List[int]) -> int:
    res, curMin, curMax = max(nums), 1, 1
    for num in nums:
        if num == 0:
            curMin, curMax = 1, 1 
            continue
        else:
            temp = curMin
            curMin = min(curMin * num, curMax * num, num)
            curMax = max(temp * num, curMax * num, num)
            
            res = max(res, curMax)
    return res