class Solution:
    def makeGood(self, s: str) -> str:
        """
        Complexities:
        Time:  O(n)
        Space: O(n)

        where n = len(s)
        """

        # base case: len(s) == 1
        if len(s) <= 1:
            return s



        stack = ""
        for letter in s:
            stack += letter

            if len(stack) >= 2 and stack[-2] != stack[-1] and stack[-2].lower() == stack[-1].lower():
                stack = stack[:-2]

        return stack




"""
        # iterate over all letters
        # - compare s[i], s[i+1]
        # - if I remove, look at s[i-1]
        i = 0
        while i <= len(s) - 2:
            if s[i] != s[i + 1] and s[i].lower() == s[i + 1].lower():
                s = s[:i] + s[i+2:]

                if i > 0:
                    i -= 1
            else:
                i += 1

        return s
"""