# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        dummyHead = ListNode(-1, head)

        beforeSeg = dummyHead
        firstInSeg = head
        lastInSeg = None
        afterSeg = None

        # Get initial values for lastInSeg and afterSeg
        curr = head
        for i in range(k):
            if i == k - 1:
                lastInSeg = curr
                afterSeg = curr.next
            elif curr is None:
                return head

            curr = curr.next
        

        # hold one before segment
        # hold last in segment
        # hold one after segment

        while lastInSeg is not None:
            # in segment, flip all links
            prev = None
            curr = beforeSeg.next
            next = beforeSeg.next.next

            for i in range(k):
                newPrev = curr
                newCurr = next
                newNext = next.next if next is not None else None

                curr.next = prev

                prev, curr, next = newPrev, newCurr, newNext

            
            beforeSeg.next = lastInSeg
            firstInSeg.next = afterSeg

            beforeSeg = firstInSeg
            firstInSeg = afterSeg

            curr = firstInSeg
            lastInSeg = None
            afterSeg = None
            for i in range(k):
                if curr is None:
                    break
                elif i == k - 1:
                    lastInSeg = curr
                    afterSeg = curr.next

                curr = curr.next

        return dummyHead.next