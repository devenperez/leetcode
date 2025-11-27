# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Complexities:
        Time:  O(n)
        Space: O(n)

        where n = total node in graph
        """

        if not root:
            return []

        arr = []
        if root.left:
            arr += self.inorderTraversal(root.left)

        arr += [root.val]

        if root.right:
            arr += self.inorderTraversal(root.right)

        return arr