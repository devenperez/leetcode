class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        string_to_transform = ""

        for letter in s:
            string_to_transform += str(ord(letter) - ord('a') + 1)
        
        for i in range(k):
            curr_sum = 0
            for digit in string_to_transform:
                curr_sum += int(digit)
            string_to_transform = str(curr_sum)

        return int(string_to_transform)