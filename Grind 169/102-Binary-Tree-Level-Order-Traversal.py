from collections import deque
def levelOrder(root):
    q, output = deque([root]), []
    if not root:
        return output
    while q:
        level = []
        for i in range(len(q)):
            top = q.popleft()
            level.append(top.val)
            if top.left:
                q.append(top.left)
            if top.right:
                q.append(top.right)
        output.append(level)
    return output