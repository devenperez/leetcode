class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Check horizontals
        for i in range(len(board)):
            inRow = [False] * 10
            
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                else:
                    if inRow[int(board[i][j])]:
                        return False
                    else:
                        inRow[int(board[i][j])] = True
            
        
        # Check verticals
        for j in range(len(board[0])):
            inColumn = [False] * 10
            
            for i in range(len(board)):
                if board[i][j] == ".":
                    continue
                else:
                    if inColumn[int(board[i][j])]:
                        return False
                    else:
                        inColumn[int(board[i][j])] = True
        
        # Check boxes
        for boxI in range(3):
            for boxJ in range(3):
                inBox = [False] * 10
                for i in range(3):
                    for j in range(3):
                        if board[(boxI * 3) + i][(boxJ * 3) + j] == ".":
                            continue
                        else:
                            if inBox[int(board[(boxI * 3) + i][(boxJ * 3) + j])]:
                                return False
                            else:
                                inBox[int(board[(boxI * 3) + i][(boxJ * 3) + j])] = True
                
        return True