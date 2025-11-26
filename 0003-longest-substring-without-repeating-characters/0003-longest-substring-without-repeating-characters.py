class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """
        Complexities:
        Time:  O(n)
        Space: O(X)

        where n = len(s)
              X = len([All compatible characters])
        """

        charsInSubstring = set({})

        startIndex = 0  # inclusive
        endIndex = 0    # exclusive
        maxLengthFound = 0

        # Use sliding window to find solution
        # - O(n) -> startIndex or endIndex always increase by 1 every iteration = 2n
        while endIndex < len(s):
            # if next letter not in substring, then endIndex++
            if s[endIndex] not in charsInSubstring:
                charsInSubstring.add(s[endIndex])
                endIndex += 1

                # Update maxLengthFound
                if endIndex - startIndex > maxLengthFound:
                    maxLengthFound = endIndex - startIndex
            
            # else pop off front until popped [next letter]
            else:
                while s[startIndex] != s[endIndex]:
                    charsInSubstring.remove(s[startIndex])
                    startIndex += 1

                charsInSubstring.remove(s[startIndex])
                startIndex += 1

        return maxLengthFound