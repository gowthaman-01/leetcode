class Solution:
    def isSymmetric(self, root):
        self.mirror = True
        self.helper(root.left, root.right)
        return self.mirror

    def helper(self, left, right):
        if not left and not right:
            return
        elif not left or not right:
            self.mirror = False
            return
        if left.val != right.val:
            self.mirror = False
            return
        self.helper(left.right, right.left)
        self.helper(left.left, right.right)
