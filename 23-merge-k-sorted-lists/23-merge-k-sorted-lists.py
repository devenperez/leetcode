# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # Remove empty lists
        lists = list(filter(lambda x : False if x == None else True, lists))
        
        # Base Case:
        if len(lists) == 0:
            return None
        
        firstOfAllLists = list(map(lambda x : x.val, lists))
        rootNode = None
        currentNode = None
        
        while len(lists) > 0:
            lowestVal = min(firstOfAllLists)
            indexWithLowest = firstOfAllLists.index(lowestVal)
            nextNode = ListNode(lowestVal)
            
            if currentNode == None:
                # Initialize nodes (runs once on first iter.)
                rootNode = nextNode
                currentNode = nextNode
            else:
                # Iterate through nodes
                currentNode.next = nextNode
                currentNode = nextNode
            
            # Remove lowest value from lists
            lists[indexWithLowest] = lists[indexWithLowest].next

            # Replace lowest value with next in list
            if lists[indexWithLowest] == None:
                lists.pop(indexWithLowest)
                firstOfAllLists.pop(indexWithLowest)
            else:
                firstOfAllLists[indexWithLowest] = lists[indexWithLowest].val
            
            
        return rootNode
            
        