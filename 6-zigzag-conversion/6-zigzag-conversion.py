class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        # Base case: numRows = 1
        if numRows == 1:
            return s

        output = ""
        interval = (2 * numRows) - 2
        for row in range(numRows):
            letterIndex = row
            diagonalIndex = (2 * numRows) - row - 2
            while letterIndex < len(s):
                # Gets letters in vertical lines
                output += s[letterIndex]
                letterIndex += interval

                # Top and bottom rows have no diagonal pieces
                if row == 0 or row == numRows - 1:
                    continue

                # Catch end of string
                if diagonalIndex >= len(s):
                    break
                
                # Gets letters on diagonals
                output += s[diagonalIndex]
                diagonalIndex += interval

        return output

