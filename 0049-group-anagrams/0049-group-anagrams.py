class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Complexities
        Time:  O(Mn)
        Space: O(n)
        
        where n = len(strs)
              M = max(len(str[i])
        """


        # Store strs in dictionary, keyed by sorted string (or frequency count)
        strsByAnagram = dict({})

        # Conversion helper - O(M)
        def toFreqTuple(s: str):
            freq = [0] * 26
            for l in s:
                letter_index = ord(l) - ord('a')
                freq[letter_index] += 1
            return tuple(freq) 


        # Map each s in str to its key - O(Mn)
        for s in strs:
            key = toFreqTuple(s)
            strsByAnagram[key] = [*strsByAnagram.get(key, []), s]

        # Convert dict to array to return - O(n)
        return list(strsByAnagram.values())