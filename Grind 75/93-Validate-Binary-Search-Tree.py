from math import *
class Solution:
    def check(self, node, limit):
        if not node:
            return True
        lower, upper = limit[0], limit[1]
        if node.val <= lower or node.val >= upper:
            return False
        if self.check(node.left, (lower, node.val)) and self.check(node.right, (node.val, upper)):
            return True
        return False
    
    
    
    def isValidBST(self, root) -> bool:
        if not root:
            return False
        if self.check(root.left, (float(-inf), root.val)) and self.check(root.right, (root.val, float(inf))):
            return True
        return False
    