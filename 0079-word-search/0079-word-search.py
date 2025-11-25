class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        startPoints = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    startPoints.append((i, j))

        def recur(i, j, restWord, seen):
            if len(restWord) == 0:
                return True

            foundSolution = False

            if i - 1 >= 0:
                if board[i - 1][j] == restWord[0]:
                    if (i - 1, j) not in seen:
                        foundSolution |= recur(i - 1, j, restWord[1:], seen.union({(i - 1, j)}))
            if j - 1 >= 0:
                if board[i][j - 1] == restWord[0]:
                    if (i, j - 1) not in seen:
                        foundSolution |= recur(i, j - 1, restWord[1:], seen.union({(i, j - 1)}))

            if i + 1 < len(board):
                if board[i + 1][j] == restWord[0]:
                    if (i + 1, j) not in seen:
                        foundSolution |= recur(i + 1, j, restWord[1:], seen.union({(i + 1, j)}))
            if j + 1 < len(board[i]):
                if board[i][j + 1] == restWord[0]:
                    if (i, j + 1) not in seen:
                        foundSolution |= recur(i, j + 1, restWord[1:], seen.union({(i, j + 1)}))

            return foundSolution

        for sp in startPoints:
            if recur(sp[0], sp[1], word[1:], set({(sp[0], sp[1])})):
                return True
        
        return False
        