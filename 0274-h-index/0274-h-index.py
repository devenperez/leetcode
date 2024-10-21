class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        n = len(citations)
        maxSoFar = 0
        for i, x in enumerate(citations):
            if i + 1 >= x:
                maxSoFar = max(maxSoFar, x)
            else:
                maxSoFar = max(maxSoFar, i + 1)
        
        return maxSoFar