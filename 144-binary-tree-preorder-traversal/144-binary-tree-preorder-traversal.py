# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Base cases: no node or only root node
        if root == None:
            return []
    
        if root.left == None and root.right == None:
            return [root.val]
        
        # Simple recursive solution: add to array as you traverse
        visited = [root.val]    # First node in the order is the current one
        
        # All nodes to the left must be added next in the array
        if root.left != None:
            visited += self.preorderTraversal(root.left)
            
        # All nodes to the right must be added next in the array
        if root.right != None:
            visited += self.preorderTraversal(root.right)
            
        return visited
        
        
        