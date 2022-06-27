def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        # If we are in the left sorted array
        if nums[m] >= nums[l]:
            if target >= nums[l] and target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        # If we are in the right sorted array
        else:
            if target <= nums[r] and target > nums[m]:
                l = m + 1
            else:
                r = m - 1
    return -1
