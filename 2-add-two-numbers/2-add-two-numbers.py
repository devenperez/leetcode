# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = ListNode((l1.val + l2.val) % 10)
        carry = (l1.val + l2.val) / 10
        follow = sum
        num1 = l1.next
        num2 = l2.next
        while num1 != None or num2 != None or carry > 0:
            if num1 == None and num2 == None:
                follow.next = ListNode(carry)
                carry = 0
            elif num1 == None:
                follow.next = ListNode((num2.val + carry) % 10)
                follow = follow.next
                carry = (num2.val + carry) / 10
                num2 = num2.next
            elif num2 == None:
                follow.next = ListNode((num1.val + carry) % 10)
                follow = follow.next
                carry = (num1.val + carry) / 10
                num1 = num1.next
            else:
                follow.next = ListNode((num1.val + num2.val + carry) % 10)
                follow = follow.next
                carry = (num1.val + num2.val + carry) / 10
                num1 = num1.next
                num2 = num2.next
        return sum