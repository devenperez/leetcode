class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Conversions in decending order
        numConv = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romConv = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        
        # Conversions
        roman = ""
        for i in range(len(numConv)):
            while num >= numConv[i]:
                roman += romConv[i]
                num -= numConv[i]
        
        return roman