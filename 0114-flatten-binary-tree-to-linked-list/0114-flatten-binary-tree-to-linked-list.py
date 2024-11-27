# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flattenRecur(r: Optional[TreeNode]) -> (Optional[TreeNode], Optional[TreeNode]):
            if (r is None or (r.left is None and r.right is None)):
                rValStr = r.val if r is not None else "None"
                print(f"{rValStr} -> ({rValStr}, {rValStr})")
                return (r, r)
            
            leftFlat = flattenRecur(r.left)
            rightFlat = flattenRecur(r.right)

            r.left = None

            if leftFlat[0] is None:
                r.right = rightFlat[0]
            else:
                r.right = leftFlat[0]
                leftFlat[1].right = rightFlat[0]

            end = rightFlat[1] if rightFlat[1] is not None else leftFlat[1]

            rtValStr = end.val if end is not None else "None"
            print(f"{r.val} -> ({r.val}, {rtValStr})")
            return (r, end)

        flattenRecur(root)