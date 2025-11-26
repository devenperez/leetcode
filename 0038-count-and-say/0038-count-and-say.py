class Solution:
    def countAndSay(self, n: int) -> str:
        """
        Complexities:
        Time:  O(n2^n)
        Space: O()
        """

        # O(len(s)) where len(s) ~ O(2^n) 
        def RLE(s: str) -> str:
            rle = ""
            checkChar = s[0]
            charCount = 0
            for i, l in enumerate(s):
                if checkChar == l:
                    charCount += 1
                else:
                    rle += f"{charCount}{checkChar}"
                    checkChar = l
                    charCount = 1

            if checkChar:
                rle += f"{charCount}{checkChar}"

            return rle

        lastSol = "1"
        # Iteratively call RLE on lastSol (equiv. to countAndSay(n-1))
        # - O(n2^n) = n * O(2^n)
        for i in range(2, n + 1):
            lastSol = RLE(lastSol)

        return lastSol
