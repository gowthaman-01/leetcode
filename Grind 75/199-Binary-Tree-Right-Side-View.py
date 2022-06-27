from collections import deque


def rightSideView(root):
    if not root:
        return None
    output, q = [], deque([root])
    while q:
        last = len(q) - 1
        for i in range(len(q)):
            top = q.popleft()
            if i == last:
                output.append(top.val)
            if top.left:
                q.append(top.left)
            if top.right:
                q.append(top.right)
    return output
