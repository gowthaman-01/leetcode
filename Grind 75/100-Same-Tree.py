def isSameTree(p, q):
    same = True

    def dfs(node1, node2):
        if not same:
            return
        if not node1 and not node2:
            return
        if not node1 or not node2:
            same = False
            return
        if node1.val != node2.val:
            same = False
            return
        dfs(node1.left, node2.left)
        dfs(node1.right, node2.right)
    dfs(p, q)
    return same
