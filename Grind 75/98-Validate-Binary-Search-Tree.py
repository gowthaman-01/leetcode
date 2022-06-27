def check(node, limit):
    if not node:
        return True
    lower, upper = limit[0], limit[1]
    if node.val <= lower or node.val >= upper:
        return False
    if check(node.left, (lower, node.val)) and check(node.right, (node.val, upper)):
        return True
    return False


def isValidBST(root):
    if not root:
        return False
    if check(root.left, (float(-inf), root.val)) and check(root.right, (root.val, float(inf))):
        return True
    return False
