from collections import deque
class Solution:
    def widthOfBinaryTree(self, root):
        if not root: return 0
        q, res = deque([(root, 1)]), 1
        while q:
            left, right, new = None, None, False
            for i in range(len(q)):
                top = q.popleft()
                node, pos = top[0], top[1]
                if node.left:
                    npos = pos * 2 - 1
                    if left == None or npos < left:
                        left = npos
                    if right == None or npos > right:
                        right = npos
                    q.append((node.left, npos))
                if node.right:
                    npos = pos * 2
                    if left == None or npos < left:
                        left = npos
                    if right == None or npos > right:
                        right = npos
                    q.append((node.right, npos))
                if node.right != None or node.left != None:
                    new = True
            if not new:
                return res
            res = max(res, right - left + 1)
        return res