class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # All negative numbers are not palindromes
        if x < 0:
            return False
        
        # Avoids math log error
        if x == 0:
            return True
        
        currPower = int(math.log(x, 10))
        while currPower >= 1:
            firstDigit = x / (10 ** currPower)
            lastDigit  = x % 10
            
            if firstDigit != lastDigit:
                return False
            
            # Remove first and last digit
            x -= firstDigit * (10 ** currPower)
            x /= 10
            currPower -= 2
            
        # True if x is one digit (or widdled down to it)
        return True
            