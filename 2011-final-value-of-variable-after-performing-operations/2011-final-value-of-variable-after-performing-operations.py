class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        value = 0
        
        for op in operations:
            if op[1] == "+":
                value += 1
            else:
                value -= 1
                
        return value