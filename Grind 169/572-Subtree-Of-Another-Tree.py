class Solution:
    def isSubtree(self, root, subRoot):
        def comparision(root1, root2):
            if not root1 and not root2:
                return
            if not root1 or not root2:
                self.sub = False
                return
            if root1.val != root2.val:
                self.sub = False
                return
            comparision(root1.left, root2.left)
            comparision(root1.right, root2.right)

        def dfs(node):
            if self.sub:
                return
            if not node:
                return
            if node.val == self.subRoot.val:
                self.sub = True
                comparision(node, subRoot)
            dfs(node.right)
            dfs(node.left)

        self.sub = False
        self.subRoot = subRoot

        dfs(root)
        return self.sub
