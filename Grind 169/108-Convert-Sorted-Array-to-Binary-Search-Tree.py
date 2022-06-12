class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums):
    def fill(nums):
        if not nums:
            return None
        if len(nums) == 1:
            node = TreeNode(nums[0], None, None)
            return node

        middle = len(nums) // 2

        if middle - 1 >= 0:
            left = nums[0: middle]
        else:
            left = None

        if middle + 1 < len(nums):
            right = nums[middle + 1: len(nums)]
        else:
            right = None

        node = TreeNode(nums[middle], fill(left), fill(right))
        return node

    return fill(nums)
