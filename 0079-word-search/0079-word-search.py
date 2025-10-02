class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def existFromStart(x: int, y: int, wordLeft: str, used: Set[Tuple[int, int]]):
            if len(wordLeft) == 0:
                return True

            if board[x][y] != wordLeft[0]:
                return False

            if len(wordLeft) == 1:
                return True

            newUsed = used.union(set([(x, y)]))

            if x + 1 < len(board) and (x+1,y) not in used and existFromStart(x + 1, y, wordLeft[1:], newUsed):
                return True
            
            if x - 1 >= 0 and (x-1,y) not in used and existFromStart(x - 1, y, wordLeft[1:], newUsed):
                return True

            if y + 1 < len(board[x]) and (x,y+1) not in used and existFromStart(x, y + 1, wordLeft[1:], newUsed):
                return True
            
            if y - 1 >= 0 and (x,y-1) not in used and existFromStart(x, y - 1, wordLeft[1:], newUsed):
                return True

            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if existFromStart(i, j, word, set({})):
                    return True

        return False
            