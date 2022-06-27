def maxArea(height):
    l, r = 0, len(height) - 1
    current = (r - l) * min(height[r], height[l])
    max_area = current
    while l < r:
        if height[l] < height[r]:
            l += 1
            current = (r - l) * min(height[r], height[l])
            max_area = max(current, max_area)

        else:
            r -= 1
            current = (r - l) * min(height[r], height[l])
            max_area = max(current, max_area)

    return max_area
