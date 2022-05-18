class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = [x for x in s]
        longestLength = 1
        
        if len(letters) == 0: return 0
        
        for i in range(len(letters)):
            dictionary = {}
            for j in range(i, len(letters)):
                if dictionary.get(letters[j]) == None:
                    dictionary[letters[j]] = 0
                else:
                    if j-i > longestLength:
                        longestLength = j-i
                    break
                    
                if j == len(letters) - 1:
                    if j-i+1 > longestLength:
                        longestLength = j-i+1
                        return longestLength
        return longestLength