def sortColors(nums):
    red, white, blue = 0, 0, 0
    for num in nums:
        if num == 0:
            red += 1
        elif num == 1:
            white += 1
        else:
            blue += 1
    pos = len(nums) - 1
    while pos >= 0:
        if blue > 0:
            nums[pos] = 2
            blue -= 1
        elif white > 0:
            nums[pos] = 1
            white -= 1
        else:
            nums[pos] = 0
        pos -= 1
    return nums
