class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = -1
        if digits[-1] == 9:
            digits[-1] = 0
            i = -2
            if abs(i) > len(digits):
                digits.insert(0, 1)
                return digits
            while digits[i] == 9:
                digits[i] = 0
                if abs(i - 1) > len(digits):
                    digits.insert(0, 1)
                    return digits
                i -= 1
                  
        digits[i] += 1
        return digits
            
                
            
        