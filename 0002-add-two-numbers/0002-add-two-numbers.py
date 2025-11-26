# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Complexities:
        Time:  O(n)
        Space: O(1)

        where n = max(len(l1), len(l2))
        """

        # Addition by place value
        currNode1 = l1
        currNode2 = l2
        sumNode = None
        tailNode = None
        carry = 0
        placeValue = 1

        # Loop through nodes until reached end of both lists
        while currNode1 or currNode2:
            v1 = currNode1.val if currNode1 else 0 
            v2 = currNode2.val if currNode2 else 0 

            sumVal = (v1 + v2 + carry) * placeValue
            val = sumVal % 10
            carry = sumVal // 10
            newNode = ListNode(val)
            
            if sumNode == None:
                sumNode = newNode
            else:
                tailNode.next = newNode

            tailNode = newNode

            currNode1 = currNode1.next if currNode1 else None
            currNode2 = currNode2.next if currNode2 else None

        if carry:
            tailNode.next = ListNode(carry)

        return sumNode or ListNode(0)
        
        