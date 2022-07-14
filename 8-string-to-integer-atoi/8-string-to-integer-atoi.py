class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        numStr = ""
        
        # Remove whitespace
        s = s.strip()
        
        # End on empty string
        if s == "":
            return 0
        
        # Check for sign
        if s[0] in "+-":
            numStr += s[0]
            s = s[1:]
        
        # Extract only the digits
        while len(s) > 0 and s[0] in "0123456789":
            numStr += s[0]
            s = s[1:]
            
        # End on empty string
        if numStr == "" or numStr == "+" or numStr == "-":
            return 0
            
        # Contrain integer to [-2^31, 2^31 - 1]
        integer = int(numStr)
        if integer < -2 ** 31:
            integer = -2 ** 31
        elif integer >= 2 ** 31:
            integer = (2 ** 31) - 1
            
        return integer
            
        