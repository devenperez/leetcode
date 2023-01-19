# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # Gets next node in traversal (and removes it from the string)
        #   Returns (value, depth)
        def getNextNode() -> tuple[int, int]:
            nonlocal traversal
            
            # Find depth
            depth = 0
            while traversal[0] == "-":
                depth += 1
                traversal = traversal[1:]
                
            # Find value
            value = 0
            while len(traversal) > 0 and traversal[0] != "-":
                value = (value * 10) + int(traversal[0])
                traversal = traversal[1:]
                
            return (value, depth)
        
        # Base Case: empty tree
        if len(traversal) == 0:
            return None
        
        root = TreeNode(getNextNode()[0])
        currentRoute = [root]
        
        while len(traversal) > 0:
            nodePair = getNextNode()
            
            # Go deeper
            if nodePair[1] == len(currentRoute):
                currentRoute[-1].left = TreeNode(nodePair[0])
                currentRoute.append(currentRoute[-1].left)
                continue
                
            # Go back up the tree
            while nodePair[1] < len(currentRoute):
                currentRoute.pop()
            
            currentRoute[-1].right = TreeNode(nodePair[0])
            currentRoute.append(currentRoute[-1].right)
            
        return root