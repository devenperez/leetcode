class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Recursive solution
        
        # Base Case
        if s == "" or p == "":
            if s == "" and p == "":
                return True
            # Check for "*" = 0 elements
            elif s == "" and len(p) >= 2 and p[1] == "*":
                return self.isMatch(s,p[2:])   
            else:
                return False
        
        # Dealing with "*"
        if len(p) >= 2 and p[1] == "*":
            
            # Next character compatable with wildcard
            if s[0] == p[0] or p[0] == ".":
                return (self.isMatch(s,p[2:]) or    # End wildcard
                        self.isMatch(s[1:],p))      # Use character as wildcard
            else:
                return self.isMatch(s,p[2:])
            
            
        # Dealing with "."
        if p[0] == ".":
            return self.isMatch(s[1:],p[1:])    
        
        
        # Check first letters, recurse on the rest
        if s[0] == p[0]:
            return self.isMatch(s[1:],p[1:])
            