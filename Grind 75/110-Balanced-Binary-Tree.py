def isBalanced(root):
    balanced = True

    def checker(root, height):
        if not root:
            return height - 1
        left_height = checker(root.left, height + 1)
        right_height = checker(root.right, height + 1)
        difference = abs(left_height - right_height)
        if difference > 1:
            balanced = False
        return max(left_height, right_height)
    checker(root, 0)
    return balanced
