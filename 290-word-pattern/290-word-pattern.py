class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        letterToWord = {}
        
        # Lengths do not match
        if len(words) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            # First iteration of a letter in pattern
            if pattern[i] not in letterToWord:
                # Word cannot be represented by multiple letters
                if words[i] in letterToWord.values():
                    return False
                
                letterToWord[pattern[i]] = words[i]
                continue
            
            # Does word match pattern
            if letterToWord[pattern[i]] != words[i]:
                return False
            
        return True