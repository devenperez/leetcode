class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Empty needle edge-case
        if needle == "":
            return 0
        
        index = 0
        while index + len(needle) <= len(haystack):
            if haystack[index] == needle[0]:
                if haystack[index:index+len(needle)] == needle:
                    return index
            index += 1
            
        return -1