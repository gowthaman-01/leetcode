def maxSubArray(nums):
    total, current = None, None
    for num in nums:
        if current == None:
            current = num
        else:
            current += num
        if current < 0 and num < 0:
            if total == None:
                total = current
            else:
                total = max(total, current)
            current = None
        else:
            if total == None:
                total = current
            else:
                total = max(current, total)
    return total
