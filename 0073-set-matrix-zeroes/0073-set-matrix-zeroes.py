class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # O(m+n) space
        rowsToZero = set()
        colsToZero = set()

        # Find all zeros
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rowsToZero.add(i)
                    colsToZero.add(j)

        # Zero rows and cols as needed
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in rowsToZero or j in colsToZero:
                    matrix[i][j] = 0 