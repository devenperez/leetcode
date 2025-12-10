"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        newHead = Node(node.val)

        frontier = deque([ node ])
        nodeMapping = { node.val: newHead }
        while len(frontier) > 0:
            current = frontier.popleft()

            for n in current.neighbors:
                if n.val not in nodeMapping:
                    newNode = Node(n.val)
                    nodeMapping[newNode.val] = newNode
                    frontier.append(n)
                nodeMapping[current.val].neighbors.append(nodeMapping[n.val])

        return newHead
        
