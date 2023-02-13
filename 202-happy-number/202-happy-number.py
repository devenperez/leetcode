class Solution:
    def isHappy(self, n: int) -> bool:
        def sumSquareDigits(x: int) -> int:
            sum = 0
            while x > 0:
                sum += (x % 10) ** 2
                x = int(x / 10)
            return sum
        
        used = set({n})
        n = sumSquareDigits(n)
        
        while n != 1:
            if n in used:
                return False
            used.add(n)
            n = sumSquareDigits(n)
        
        return True