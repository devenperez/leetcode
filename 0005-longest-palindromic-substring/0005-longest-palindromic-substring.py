class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Complexities:
        Time:  O(n^3)
        Space: O(1)

        where n = len(s)
        """

        # indicies inclusive - O(n)
        def isPalindrome(startIndex: int, endIndex: int):
            if startIndex >= endIndex:
                return True

            if s[startIndex] == s[endIndex]:
                return isPalindrome(startIndex + 1, endIndex - 1)
            return False


        maxPalindrome = s[0]
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                length = j - i + 1
                if length > len(maxPalindrome) and isPalindrome(i, j):
                    maxPalindrome = s[i:j+1]

        return maxPalindrome

