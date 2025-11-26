class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Complexities:
        Time:  O(n^2)
        Space: O(1)

        where n = len(s)
        """

        # Returns the longest palindrome centered at s[i] or (s[i], s[i + 1])
        # - O(n)
        def longestPalindromeFromCenter(i: int, evenCentered: bool):
            offset = 1
            evenOffset = 1 if evenCentered else 0

            while i - offset >= 0 and i + offset + evenOffset < len(s) and s[i - offset] == s[i + offset + evenOffset]:
                offset += 1

            offset -= 1 # Account for off-by-one

            return s[i - offset : i + offset + evenOffset + 1]

        maxPalindrome = s[0]
        # For each letter, check if it is the center of a palindrome (or center with s[i+1])
        # - O(n^2) = n * 2(O(n))
        for i in range(len(s)):
            # Check for an even length palindrome
            if i + 1 < len(s) and s[i] == s[i+1]:
                evenPalindrome = longestPalindromeFromCenter(i, True)

                if len(evenPalindrome) > len(maxPalindrome):
                    maxPalindrome = evenPalindrome
            
            oddPalindrome = longestPalindromeFromCenter(i, False)
            if len(oddPalindrome) > len(maxPalindrome):
                    maxPalindrome = oddPalindrome


        return maxPalindrome

