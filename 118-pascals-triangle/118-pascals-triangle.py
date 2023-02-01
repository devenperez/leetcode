class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        triangle = [[1],[1,1]]
        
        while len(triangle) < numRows:
            nextRow = [((triangle[-1][i] + triangle[-1][i - 1]) if (i in range(1,len(triangle[-1]))) else 1) for i in range(len(triangle[-1]) + 1)]
            triangle.append(nextRow)
            
        return triangle