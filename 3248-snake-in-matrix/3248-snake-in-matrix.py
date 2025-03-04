class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        movesCount = {
            "RIGHT": 0,
            "LEFT": 0,
            "UP": 0,
            "DOWN": 0,
        }
        for command in commands:
            movesCount[command] += 1

        return movesCount["RIGHT"] - movesCount["LEFT"] + n * (movesCount["DOWN"] - movesCount["UP"])