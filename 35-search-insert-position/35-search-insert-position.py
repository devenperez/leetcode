class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while end - start > 0:
            midpoint = int((end - start) / 2) + start
            
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] > target:
                end = midpoint - 1
            else:
                start = midpoint + 1
                
        if nums[start] >= target:
            return start
        else:
            return end + 1