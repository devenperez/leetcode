class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.createSets("(", 1, n - 1)
        
    def createSets(self, current, opened, yetToOpen):
        if opened == 0 and yetToOpen == 0:
            return [current]

        returnSet = []
        if yetToOpen > 0:
            returnSet += self.createSets(current + "(", opened + 1, yetToOpen - 1)
        
        if opened > 0:
            returnSet += self.createSets(current + ")", opened - 1, yetToOpen)
            
        return returnSet