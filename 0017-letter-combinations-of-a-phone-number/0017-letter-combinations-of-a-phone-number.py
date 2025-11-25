class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        curr = [""]
        next = []

        for digit in digits:  
            for prefix in curr:
                for newChar in mapping[digit]:
                    next.append(f"{prefix}{newChar}")
            curr = next
            next = []

        return curr

        