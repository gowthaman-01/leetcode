def permute(nums):
    if len(nums) == 1:
        return [nums]
    output = []
    for i in range(len(nums)):
        possible = permute(nums[0: i] + nums[i + 1:])
        for perm in possible:
            perm += [nums[i]]
            output.append(perm)
    return output
