def checker(root, p, q):
    if root.val == p.val or root.val == q.val:
        ancestor = root
        return
    if p.val < root.val and q.val > root.val:
        ancestor = root
        return
    if p.val > root.val and q.val < root.val:
        ancestor = root
        return
    if p.val > root.val and q.val > root.val:
        checker(root.right, p, q)
    else:
        checker(root.left, p, q)


def lowestCommonAncestor(root, p, q):
    ancestor = None
    checker(root, p, q)
    return ancestor
