def diameterOfBinaryTree(root):
    maxPath = 0
    def height(node):
        if not node:
            return 0
        left = height(node.left)
        right = height(node.right)
        maxPath = max(maxPath, left + right)
        return max(left, right) + 1
    height(root)
    return maxPath
    