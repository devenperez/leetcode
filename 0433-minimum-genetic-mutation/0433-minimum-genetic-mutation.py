class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """

        def isMutation(g1, g2):
            numDiff = 0
            for i in range(len(g1)):
                if g1[i] != g2[i]:
                    numDiff += 1
                    if numDiff > 1:
                        return False
            return numDiff == 1

        if endGene not in bank:
            return -1

        queue = [(startGene, 0)]
        seen = [False] * len(bank)

        while len(queue) > 0:
            currentGene, currentDistance = queue.pop(0)
            
            for i, gene in enumerate(bank):
                if seen[i]: 
                    continue

                if isMutation(currentGene, gene):
                    if gene == endGene:
                        return currentDistance + 1

                    queue.append((gene, currentDistance + 1))
                    seen[i] = True

        return -1