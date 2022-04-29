from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        q = deque()
        output = []
        
        if not root:
            return output
        
        q.append(root)
        
        while q:
            current = []
            qlen = len(q)
            
            for i in range(qlen):
                t = q.popleft()
                if t: 
                    current.append(t.val)
                    q.append(t.left)
                    q.append(t.right)
                    
            if current:
                output.append(current)
        
        return output