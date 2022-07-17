class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        said = "1"
        for i in range(2, n + 1):
            counting = 0
            countedN = 0
            newSaid = ""
            for a in range(len(said)):
                if said[a] != counting:
                    if counting != 0:
                        newSaid += str(countedN) + str(counting) 
                    counting = said[a]
                    countedN = 1
                else:
                    countedN += 1
        
            newSaid += str(countedN) + str(counting)
            said = newSaid
            
        return said