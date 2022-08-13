class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        oldIndex = 1
        newIndex = 1
        lastNum = nums[0]
        
        while oldIndex < len(nums):
            if nums[oldIndex] == lastNum:
                oldIndex += 1
            else:
                nums[newIndex] = nums[oldIndex]
                newIndex += 1
                lastNum = nums[oldIndex]
        
        return len(nums[:newIndex])