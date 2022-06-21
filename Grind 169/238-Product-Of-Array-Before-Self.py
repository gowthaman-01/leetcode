def productExceptSelf(nums):
    output = [1 for num in nums]
    prefix = 1
    for i, num in enumerate(nums):
        output[i] *= prefix
        prefix *= num

    pos = len(nums) - 1
    postfix = 1
    while pos >= 0:
        output[pos] *= postfix
        postfix *= nums[pos]
        pos -= 1
    return output
