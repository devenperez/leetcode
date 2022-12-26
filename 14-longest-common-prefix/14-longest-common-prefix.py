class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Base len(strs) = 1 case:
        if len(strs) == 1:
            return strs[0]
        
        # Case len(strs) >= 2
        currentLCP = self.lcpPair(strs[0], strs[1])
        for i in range(2, len(strs)):
            # All 0-i strings have no common prefix, thus neither will 0-n
            if currentLCP == "":
                return ""
            
            # Refine currentLCP to include the i'th element
            currentLCP = self.lcpPair(currentLCP, strs[i])
        
        return currentLCP
    
    # Finds the longest common prefix of two strings
    def lcpPair(self, s1, s2):
        commonPrefixLength = 1
        while s1[:commonPrefixLength] == s2[:commonPrefixLength] and commonPrefixLength <= min(len(s1), len(s2)):
            commonPrefixLength += 1
        return s1[:(commonPrefixLength - 1)]
                