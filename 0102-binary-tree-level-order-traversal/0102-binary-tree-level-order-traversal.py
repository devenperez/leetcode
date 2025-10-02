# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        outNodes = [[root]]
        out = [[root.val]]
        nextHasChildren = root.left is not None or root.right is not None

        while nextHasChildren:
            nextHasChildren = False
            nextLevel = []
            nextLevelNodes = []

            for node in outNodes[-1]:
                if node.left is not None:
                    nextLevel.append(node.left.val)
                    nextLevelNodes.append(node.left)
                    nextHasChildren |= node.left.left is not None or node.left.right is not None

                if node.right is not None:
                    nextLevel.append(node.right.val)
                    nextLevelNodes.append(node.right)
                    nextHasChildren |= node.right.left is not None or node.right.right is not None
            out.append(nextLevel)
            outNodes.append(nextLevelNodes)

        return out
        
