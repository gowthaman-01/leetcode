def maxDepth(root) -> int:
    total_nodes = 0

    def checker(root, nodes):
        if not root:
            total_nodes = max(nodes - 1, total_nodes)
            return
        checker(root.left, nodes + 1)
        checker(root.right, nodes + 1)

    checker(root, 1)
    return total_nodes
