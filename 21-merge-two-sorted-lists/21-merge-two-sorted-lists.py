# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Edge case: an empty list
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        # Inititialize merged variables
        mergedHead = list1
        mergedCurrent = list1
        
        # Pick smallest node as new head node
        if list1.val > list2.val:
            mergedHead = list2
            mergedCurrent = list2
            list2 = list2.next
        else:
            list1 = list1.next
            
        # Merge lists
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                mergedCurrent.next = list1
                list1 = list1.next
            else:
                mergedCurrent.next = list2
                list2 = list2.next
            mergedCurrent = mergedCurrent.next
            
        # Attach the rest of the nodes
        if list1 == None:
            mergedCurrent.next = list2
        elif list2 == None:
            mergedCurrent.next = list1
                
        # Return merged list
        return mergedHead