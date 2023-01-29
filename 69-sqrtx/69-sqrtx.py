class Solution:
    def mySqrt(self, x: int) -> int:
        nextOdd = 1
        
        # Represent x as a sum of odd numbers
        while x >= nextOdd:
            x -= nextOdd
            nextOdd += 2
            
        return int((nextOdd - 1) / 2)
