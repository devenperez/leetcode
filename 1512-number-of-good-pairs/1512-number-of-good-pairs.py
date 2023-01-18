class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        
        while len(nums) > 0:
            oldLength = len(nums)
            
            # Removes all instances of nums[0]
            nums = [ n for n in nums if n != nums[0] ]
            
            numOccurances = oldLength - len(nums)
            
            if numOccurances > 1:
                count += int((numOccurances * (numOccurances - 1)) / 2)   # numOccurances choose 2
                
        return count
        
        """
        ## Straight-forward solution
        count = 0
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        
        return count
        """