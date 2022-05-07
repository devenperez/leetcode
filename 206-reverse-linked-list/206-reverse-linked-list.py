# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: return None
        if head.next == None: return head
        
        reversedHead = ListNode(head.val)
        oldNode = head.next
        while oldNode != None:
            reversedHead = ListNode(oldNode.val, reversedHead)
            oldNode = oldNode.next
        return reversedHead