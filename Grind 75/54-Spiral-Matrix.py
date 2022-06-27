def subsets(nums):
    output = []
    if not nums:
        return [[]]
    remaining = subsets(nums[1:])
    for possible in remaining:
        output.append(possible + [nums[0]])
        output.append(possible)
    return output
