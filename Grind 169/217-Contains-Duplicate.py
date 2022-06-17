def containsDuplicate(nums):
    h = {}
    for num in nums:
        h[num] = h.get(num, 0) + 1
        if h[num] > 1: 
            return True
    return False
    