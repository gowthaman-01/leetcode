class Solution:
    def pathSum(self, root, targetSum):
        output = []
        if not root:
            return output
        if not root.left and not root.right and targetSum == root.val:
            return [[root.val]]
        possibleLeft, possibleRight = self.pathSum(root.left, targetSum - root.val), self.pathSum(root.right, targetSum - root.val)
        for possible in possibleLeft:
            possible = [root.val] + possible
            output.append(possible) 
        for possible in possibleRight:
            possible = [root.val] + possible
            output.append(possible)
        return output
        
        