def minDepth(root):
    def dfs(node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        elif node.left and not node.right:
            return 1 + dfs(node.left)
        elif node.right and not node.left:
            return 1 + dfs(node.right)
        else:
            return min(dfs(node.left) + 1, dfs(node.right) + 1)
    return dfs(root)
