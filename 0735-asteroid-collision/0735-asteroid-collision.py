class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Complexities:
        Time:  O(n)
        Space: O(n)

        where n = len(asteroids)
        """

        # iterate left to right
        # - if right (+ve), keep stack
        # - if left (-ve), compare/consume top of stack
        # - - if left consume all of stack, add to output (it will survive)

        stack = []
        survivedAsteroids = []
        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            else:
                isDestroyed = False
                while len(stack) > 0 and abs(asteroids[i]) >= stack[-1]:
                    if abs(asteroids[i]) == stack[-1]:
                        isDestroyed = True
                        stack.pop()
                        break
                    stack.pop()
                
                if len(stack) == 0 and not isDestroyed:
                    survivedAsteroids.append(asteroids[i])


        # also return stack
        survivedAsteroids += stack

        return survivedAsteroids