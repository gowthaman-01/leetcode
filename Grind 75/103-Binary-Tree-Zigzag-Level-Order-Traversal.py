from collections import deque
class Solution:
    def zigzagLevelOrder(self, root):
        if not root: return []
        res, q, reverse = [], deque([root]), False
        while q:
            level = deque([])
            for i in range(len(q)):
                top = q.popleft()
                if reverse:
                    level.appendleft(top.val)
                else:
                    level.append(top.val)
                if top.left: q.append(top.left)
                if top.right: q.append(top.right)
            res.append(level)
            reverse = not reverse
        return res
    