class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedFilter = [False] * 26
        for c in allowed:
            allowedFilter[ord(c) - ord('a')] = True
        
        numAllowedWords = 0
        for i in range(len(words)):
            allowedWord = True
            for a in words[i]:
                if not allowedFilter[ord(a) - ord('a')]:
                    allowedWord = False
                    break
                
            if allowedWord:
                numAllowedWords += 1
            
        
        return numAllowedWords