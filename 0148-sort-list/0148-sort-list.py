# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: len <= 2
        if head == None or head.next == None:
            return head
        elif head.next.next == None:
            if head.val > head.next.val:
                large = head
                small = head.next

                small.next = large
                large.next = None
                return small
            return head

        # Find middle node
        mid = head
        end = head.next
        while end.next is not None and end.next.next is not None:
            mid = mid.next
            end = end.next.next
    
        # Detach lists
        secondHead = mid.next
        mid.next = None

        # Merge two sorted linked lists
        sortedLeft = self.sortList(head)
        sortedRight = self.sortList(secondHead)

        isLeftLower = sortedLeft.val < sortedRight.val
        mergeHead = sortedLeft if isLeftLower else sortedRight
        currentHead = mergeHead

        sortedLeft = sortedLeft.next if isLeftLower else sortedLeft
        sortedRight = sortedRight if isLeftLower else sortedRight.next
        while sortedLeft is not None and sortedRight is not None:
            isLeftLower = sortedLeft.val < sortedRight.val

            lowestNode = sortedLeft if isLeftLower else sortedRight
            sortedLeft = sortedLeft.next if isLeftLower else sortedLeft
            sortedRight = sortedRight if isLeftLower else sortedRight.next
            currentHead.next = lowestNode
            currentHead = currentHead.next

        currentHead.next = sortedLeft if sortedLeft is not None else sortedRight

        return mergeHead
