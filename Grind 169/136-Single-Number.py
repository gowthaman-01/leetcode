def singleNumber(nums):
    output = nums[0]
    for num in nums[1::]:
        output = output ^ num
    return output
