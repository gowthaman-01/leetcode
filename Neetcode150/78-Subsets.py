def helper(nums, res, cur, i):
    if i >= len(nums):
        res.append(cur.copy())
        return 
    cur.append(nums[i])
    helper(nums, res, cur, i + 1)
    cur.pop()
    helper(nums, res, cur, i + 1)
    
def subsets(nums):
    res, cur = [], []
    helper(nums, res, cur, 0)
    return res
    