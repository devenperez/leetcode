class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        openBrackets = "({["
        closedBrackets = ")}]"
        openStack = ""
        
        for ch in s:
            if ch in openBrackets:
                # Add open brackets to the stack
                openStack += ch
            else: # elif ch in closedBrackets: (Contrant given: s only contains brackets)
                # Invalid if no open brackets
                if len(openStack) == 0:
                    return False
                
                # Check that the last bracket on stack is same type as close
                if openStack[-1] == openBrackets[closedBrackets.index(ch)]:
                    openStack = openStack[:-1]
                else:
                    return False
        
        # Only true if no outstanding open brackets
        return openStack == ""