class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        largestDigit = 0
        for d in n:
            if int(d) > largestDigit:
                largestDigit = int(d)
                if largestDigit == 9:
                    return largestDigit
        return largestDigit