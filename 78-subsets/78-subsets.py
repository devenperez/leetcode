class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # All subsets can be mapped to a binary number where
        #   - the number is the same length as the list
        #   - a 1 represents the number being in the list, 0 otherwise
        
        # Example:  nums = [1,2,3]
        #   subsetBinary = 0 = 0b000 -> []
        #                = 3 = 0b011 -> [2, 3]
        #   (2 ** 3) - 1 = 7 = 0b111 -> [1, 2, 3]
        
        import math
        powerSet = []
        
        for subsetBinary in range(2 ** len(nums)):
            subset = []
            
            # Iterates exactly n times (where n is the number of 1s in the binary string)
            while subsetBinary > 0:
                indexOfFirst1 = -(math.floor(math.log2(subsetBinary)) + 1)
                
                subset.append(nums[indexOfFirst1])
    
                subsetBinary -= 2 ** (-indexOfFirst1 - 1)
        
            powerSet.append(subset)
        
        return powerSet