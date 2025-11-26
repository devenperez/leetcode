# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Complexities:
        Time:  O(n)
        Space: O(1)

        where n = len(head)
        """

        # If len(head) <= 2, already sorted
        if not head or not head.next:
            return head

        oddHead = head
        oddTail = head
        evenHead = head.next
        evenTail = head.next

        currNode = head.next.next
        isOddIndex = True

        # Set tail.next = None
        oddTail.next = None
        evenTail.next = None

        # Separate list into odd list and even list
        while currNode:
            nextNode = currNode.next
            currNode.next = None

            if isOddIndex:
                oddTail.next = currNode
                oddTail = currNode
            else:
                evenTail.next = currNode
                evenTail = currNode
            
            currNode = nextNode
            isOddIndex = not isOddIndex

        # Attach both lists
        oddTail.next = evenHead

        return oddHead
