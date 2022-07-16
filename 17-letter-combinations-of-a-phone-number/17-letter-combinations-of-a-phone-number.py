class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        numToLetters = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        
        combos = [""]
        for d in digits:
            # Build upon last set 
            comsToAdd = []
            for l in numToLetters[int(d)]:
                for combo in combos:
                    comsToAdd.append(combo + l)
            # Replace old set with new, longer combos
            combos = comsToAdd
        
        # Return blank array if no string was added
        return [] if combos == [""] else combos
        