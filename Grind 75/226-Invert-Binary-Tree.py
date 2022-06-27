def deepInvert(root):
    if root == None: 
        return
    deepInvert(root.left)
    deepInvert(root.right)
    temp = root.right
    root.right = root.left
    root.left = temp

class Solution:
    def invertTree(root):
        deepInvert(root)
        return root
        