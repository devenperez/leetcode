class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        Complexities:
        Time:  O(n)
        Space: O(n)

        where n = len(s)
        """

        bracketCount = 0
        starCount = 0
        starIndecies = []
        usedStars = 0

        # Forward pass - allocate as many *s to be (
        # - when allocating a star, always use the star that appears first
        for i, l in enumerate(s):
            if l == '(':
                bracketCount += 1
            elif l == '*':
                starCount += 1
                starIndecies.append(i)
            elif bracketCount > 0:
                bracketCount -= 1
            elif starCount > 0:
                starCount -= 1
                usedStars += 1
            else:
                return False

        # There are already matching opening/closing brackets
        # - all stars are assigned empty string
        if bracketCount == 0:
            return True

        # There are more closed brackets needed than the amount of remaining stars
        if bracketCount > 0 and bracketCount > starCount:
            return False

        # Backward pass - allocate as many *s to be )
        # - the first `usedStars` stars are considered used from the forward pass
        firstViableStar = starIndecies[usedStars]
        bracketCount = 0
        starCount = 0
        for i in range(len(s) - 1, 0, -1):
            l = s[i]

            if l == ')':
                bracketCount += 1
            elif l == '*':
                starCount += 1 if i >= firstViableStar else 0
            elif bracketCount > 0:
                bracketCount -= 1
            elif starCount > 0:
                starIndecies.pop(0)
                starCount -= 1
            else:
                return False

        return True