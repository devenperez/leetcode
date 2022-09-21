# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        currentLevel = [root] # Holds all the nodes in the current depth
        hasNewLevel = root.left != None or root.right != None # True if root has children, otherwise False
        
        # Processes all children into a new array
        while hasNewLevel:
            hasNewLevel = False
            newLevel = []
            for node in currentLevel:
                if node.left != None:
                    newLevel.append(node.left)
                    hasNewLevel = True
                if node.right != None:
                    newLevel.append(node.right)
                    hasNewLevel = True
            currentLevel = newLevel if hasNewLevel else currentLevel
            
        # Computes the sum of current level nodes
        levelSum = 0
        for node in currentLevel:
            levelSum += node.val
            
        return levelSum
        