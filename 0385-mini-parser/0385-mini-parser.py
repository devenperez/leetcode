# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        """
        Complexities:
        Time: O(n)
        Space: O(n)

        where n = len(s)
        """

        # base case: number
        if s[0] != "[":
            return NestedInteger(int(s))

        # is a list
        head = NestedInteger()
        stack = [head]

        i = 1
        while i < len(s):
            if s[i] == ",":
                i += 1
            elif s[i] == "[":
                newNestedInteger = NestedInteger()
                stack[-1].add(newNestedInteger)
                stack.append(newNestedInteger)
                i += 1
            elif s[i] == "]":
                stack.pop()
                i += 1
            else: # Is number or '-'
                # Find entire number
                j = i
                while s[j] not in ",]":
                    j += 1
                newInt = int(s[i:j])
                stack[-1].add(NestedInteger(newInt))
                i = j

        return head

