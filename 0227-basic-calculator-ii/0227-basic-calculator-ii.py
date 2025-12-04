class Solution:
    def calculate(self, s: str) -> int:
        """
        Complexities:
        Time:  O(n)
        Space: O(n)

        where n = len(s)
        """


        numbers = "0123456789"

        # Read from left to right: save in stack (full number or operator)
        # - save number
        # - on operator:
        # -- if * or /, evaluate
        # -- if + or -, wait and continue
        currentNumber = 0
        stack = []

        # Evaluate numbers and create stack (of additions + subtractions)
        for c in s + "\0":
            if c == " ":
                continue
            elif c in numbers:
                digit = int(c)
                currentNumber = (currentNumber * 10) + digit
            else:
                stack.append(currentNumber)
                currentNumber = 0

                if len(stack) >= 3 and stack[-2] in "*/":
                    rOperand = stack.pop()
                    operator = stack.pop()
                    lOperand = stack.pop()

                    if operator == "*":
                        stack.append(lOperand * rOperand)
                    elif operator == "/":
                        stack.append(int(lOperand / rOperand))

                stack.append(c)

        # Pop off null terminator
        stack.pop()

        # Evaluate all additions and subtractions from stack
        current = stack[0]
        for i in range(1, len(stack) - 1, 2):
            operator = stack[i]
            rOperand = stack[i + 1]

            if operator == "+":
                current += rOperand
            elif operator == "-":
                current -= rOperand

        return current
            