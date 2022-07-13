class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rToInt = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        mixes = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        
        num = 0
        while len(s) > 0:
            if s[:2] in mixes:
                num += mixes[s[:2]]
                s = s[2:]
            else:
                num += rToInt[s[0]]
                s = s[1:]
        
        return num