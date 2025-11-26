class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Total complexities:
        # O(mn) time
        # O(1) space

        # Prepare first row/col for marking
        firstEntry = matrix[0][0]
        # - use m[0][0] as indicator for first row and col
        NO_ZEROES_IN_FIRST_ROW_OR_COL = 1
        ZERO_IN_FIRST_ROW = 2
        ZERO_IN_FIRST_COL = 3
        ZERO_IN_FIRST_ROW_AND_COL = 4

        matrix[0][0] = NO_ZEROES_IN_FIRST_ROW_OR_COL
        if firstEntry == 0:
            matrix[0][0] = ZERO_IN_FIRST_ROW_AND_COL
        else:
            print(f"cp0")
            # Search first col for 0s - O(n)
            for i in range(1, len(matrix)):
                print(f"cp1")
                if matrix[i][0] == 0:
                    matrix[0][0] = ZERO_IN_FIRST_COL
                    break

            # Search first row for 0s - O(m)
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0:
                    if matrix[0][0] == ZERO_IN_FIRST_COL:
                        matrix[0][0] = ZERO_IN_FIRST_ROW_AND_COL
                    else:
                        matrix[0][0] = ZERO_IN_FIRST_ROW 
                    break

        # Find all zeros outside the first row/col - O(mn)
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    # Use the first row/col as markers
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero center as needed - O(mn)
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Set first row/col if needed
        if matrix[0][0] == ZERO_IN_FIRST_ROW or matrix[0][0] == ZERO_IN_FIRST_ROW_AND_COL:
            for j in range(1, len(matrix[0])):
                matrix[0][j] = 0
            
        if matrix[0][0] == ZERO_IN_FIRST_COL or matrix[0][0] == ZERO_IN_FIRST_ROW_AND_COL:
            for i in range(1, len(matrix)):
                matrix[i][0] = 0

        
        matrix[0][0] = firstEntry if matrix[0][0] == NO_ZEROES_IN_FIRST_ROW_OR_COL else 0