class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        return sum(list(map(lambda x : 1 if x[1] == "+" else -1, operations)))