# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current != None:
            next = current.next

            while next != None and current.val == next.val:
                next = next.next
            

            current.next = next
            current = next
        
        return head