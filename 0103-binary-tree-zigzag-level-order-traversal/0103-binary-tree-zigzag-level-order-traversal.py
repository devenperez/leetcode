# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Complexities:
        Time:  O(n)
        Space: O(n)

        where n = number of nodes in graph
        """

        if not root:
            return []

        traversal = [[root]]
        hasNextLevel = root.left or root.right


        # Store nodes from left to right in arrays by depth - O(n)
        while hasNextLevel:
            lastLevel = traversal[-1]
            nextLevel = []
            hasNextLevel = False

            for node in lastLevel:
                if node.left:
                    nextLevel.append(node.left)
                    hasNextLevel = hasNextLevel or bool(node.left.left or node.left.right)
                
                if node.right:
                    nextLevel.append(node.right)
                    hasNextLevel = hasNextLevel or bool(node.right.left or node.right.right)

            traversal.append(nextLevel)

        # Convert nodes to values + reverse every other level - O(n)
        valueTraversal = []
        for depth, level in enumerate(traversal):
            start = 0 if depth % 2 == 0 else len(level) - 1
            end = len(level) if depth % 2 == 0 else -1
            step = 1 if depth % 2 == 0 else -1

            nextLevelValues = []
            for i in range(start, end, step):
                nextLevelValues.append(level[i].val)
            valueTraversal.append(nextLevelValues)
                


        return valueTraversal
            

        
