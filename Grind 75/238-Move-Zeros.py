def moveZeroes(nums):
    c, n = 0, 0
    while n < len(nums):
        if nums[c] == 0:
            if nums[n] != 0:
                nums[c] = nums[n]
                nums[n] = 0
                n += 1
                c += 1
            else:
                n += 1
        else:
            c += 1
            n += 1
    return nums
