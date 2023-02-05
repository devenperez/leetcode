class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def combination(n: int, r: int) -> int:
            # n! / (n - r)!
            numerator = 1
            for i in range(n - r + 1, n + 1):
                numerator *= i
                
            # 1 / r!
            divisor = 1
            for j in range(2, r + 1):
                divisor *= j
            
            return int(numerator / divisor)
        
        return [ combination(rowIndex, i) for i in range(rowIndex + 1) ]