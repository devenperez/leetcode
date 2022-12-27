class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX_32_VALUE = 2147483648
        REVERSED_MAX_32_VALUE = 463847412
        
        # Check negative 
        isNegative = False
        if x < 0:
            x = -x
            isNegative = True
            
        # Check if reversed is outside of [-2**31, 2**31 - 1]
        if x > 10**9:
            for i in range(1, 10):
                xMod10i = x % (10**i)
                reversedMax = REVERSED_MAX_32_VALUE % (10**i)
                print("i:" + str(i) + "->" + str(xMod10i) + " " + str(reversedMax))
                if xMod10i > reversedMax:
                    return 0
                elif xMod10i < reversedMax:
                    break
            
        
        # Reverse integer
        reversedInt = 0
        while x > 0:
            reversedInt *= 10
            reversedInt += x % 10
            x = int(x / 10)
            
        return -reversedInt if isNegative else reversedInt