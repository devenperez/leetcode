class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ALL_VOWELS = set(['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'])

        indices = []
        vowels = []

        for i, letter in enumerate(s):
            if letter in ALL_VOWELS:
                indices += [i]
                vowels += [letter]

        vowels.sort(key=ord)

        newStr = ""
        j = 0

        for i, letter in enumerate(s):
            if letter in ALL_VOWELS:
                newStr += vowels[j]
                j += 1
            else:
                newStr += s[i]

        return newStr
