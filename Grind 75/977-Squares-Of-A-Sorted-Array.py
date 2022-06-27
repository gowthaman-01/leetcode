def sortedSquares(nums):
    l, r = 0, len(nums) - 1
    output = []
    while l <= r:
        if nums[l] ** 2 >= nums[r] ** 2:
            output.append(nums[l] ** 2)
            l += 1
        else:
            output.append(nums[r] ** 2)
            r -= 1
    return output[::-1]
