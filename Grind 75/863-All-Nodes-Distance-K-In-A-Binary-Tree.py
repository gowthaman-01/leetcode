from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Storing parent in a hashmap and doing a bfs from the target
class Solution1:
    def dfs(self, root, parent):
        if not root: return 
        if root.left:
            parent[root.left.val] = root
            self.dfs(root.left, parent)
        if root.right:
            parent[root.right.val] = root
            self.dfs(root.right, parent)
            
    def bfs(self, target, parent, res, k):
        q, pos, visited = deque([target]), 0, set()
        while q:
            for i in range(len(q)):
                top = q.popleft()
                if top not in visited:
                    visited.add(top)
                    if pos == k:
                        res.append(top.val)
                        continue
                    if top.left:
                        q.append(top.left)
                    if top.right:
                        q.append(top.right)
                    if top.val in parent:
                        q.append(parent[top.val])
            pos += 1
                
    def distanceK(self, root: TreeNode, target: TreeNode, k: int):
        parent, res = {}, []
        self.dfs(root, parent)
        self.bfs(target, parent, res, k)
        return res
    
# Checking the distance from target and appending the appropriate nodes into result 
class Solution2:
    def search(self, root, res, target, k):
        if not root: return None
        if root == target:
            self.add(root, res, k)
            return 1  
        left, right = self.search(root.left, res, target, k), self.search(root.right, res, target, k)
        if not left and not right: return None
        if left:
            if left == k: res.append(root.val)
            self.add(root.right, res, k - 1 - left)
            return left + 1
        if right:
            if right == k: res.append(root.val)
            self.add(root.left, res, k - 1 - right)
            return right + 1   
        
    def add(self, node, res, k):
        if not node: return
        if k == 0:
            res.append(node.val)
            return 
        self.add(node.left, res, k - 1)
        self.add(node.right, res, k - 1)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int):
        res = []
        self.search(root, res, target, k)
        return res