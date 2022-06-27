def threeSum(nums):
    nums.sort()
    output = []
    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1]:
            continue
        l, r, target = i + 1, len(nums) - 1, 0 - num
        while l < r:
            if nums[l] + nums[r] == target:
                triplet = [num, nums[l], nums[r]]
                output.append(triplet)
                l += 1
                while(nums[l] == nums[l - 1] and l < r):
                    l += 1
            elif nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
    return output
