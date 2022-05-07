# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        # Get length
        counterNode = head
        length = 0
        while counterNode != None:
            counterNode = counterNode.next
            length = length + 1
        
        # Readjust
        if length == 1: return None
        if length == n: return head.next
        nodeBefore = head
        for i in range(length - n - 1):
            nodeBefore = nodeBefore.next
        if n == 1: 
            nodeBefore.next = None
        else:
            nodeBefore.next = nodeBefore.next.next
        
        return head