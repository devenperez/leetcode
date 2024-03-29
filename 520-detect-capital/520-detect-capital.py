class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word == word.upper():
            return True
        
        if word[1:] == word[1:].lower():
            return True
        
        return False