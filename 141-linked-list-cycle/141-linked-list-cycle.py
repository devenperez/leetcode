# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None: 
            return False
        
        myDict = {head: 0}
        point = head
        while point != None:
            point = point.next
            if myDict.get(point) == None:
                myDict[point] = 0
            else:
                return True
        
        return False