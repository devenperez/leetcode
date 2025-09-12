class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isVowel(c):
            return len(c) == 1 and c in "aeiou"

        # Count vowels
        numVowels = sum(map(isVowel, s))

        return numVowels > 0