class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        # Counts the number of iterations of each difficulty
        countByDifficulty = {}
        for dif in tasks:
            if dif not in countByDifficulty:
                countByDifficulty[dif] = 0
            countByDifficulty[dif] += 1
            
        # Count the amount of rounds required to complete
        roundsRequired = 0
        for count in countByDifficulty.values():
            if count == 1:
                return -1
            
            if count % 3 == 0:
                roundsRequired += count / 3
            else:
                ## Examples: 7 (rem 1), 8 (rem 2)
                # 7 = 3+2+2
                # 8 = 3+3+2
                roundsRequired += int(count / 3) + 1 
                
        return roundsRequired
                