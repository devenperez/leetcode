class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Base cases
        if len(nums) == 0:
            return [-1,-1]
        
        if nums[0] > target:
            return [-1,-1]
        
        if nums[-1] < target:
            return [-1,-1]
        
        if len(nums) == 1:
            return [0,0] if nums[0] == target else [-1,-1]
        
        foundIndex = -1
        
        # Searchable region bounds
        searchLow = 0
        searchHigh = len(nums) - 1
        
        # Find an instance of target
        while searchLow < searchHigh:
            # Base case: length of bounds = 1
            if searchHigh - searchLow == 1:
                if nums[searchLow] == target:
                    foundIndex = searchLow
                elif nums[searchHigh] == target:
                    foundIndex = searchHigh
                break
            
            # Standard search
            midpointIndex = int((searchHigh - searchLow) / 2) + searchLow
            if nums[midpointIndex] == target:
                foundIndex = midpointIndex
                break
            elif nums[midpointIndex] < target:
                searchLow = midpointIndex
            else:
                searchHigh = midpointIndex
                
        # Target not found
        if nums[foundIndex] != target:
            return [-1,-1]
                
        # Find all occurances of target
        firstOcc = foundIndex
        lastOcc = foundIndex
        while firstOcc - 1 >= 0 and nums[firstOcc - 1] == target:
            firstOcc -= 1
            
        while lastOcc + 1 < len(nums) and nums[lastOcc + 1] == target:
            lastOcc += 1
            
        return [firstOcc, lastOcc]