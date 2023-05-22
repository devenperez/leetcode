class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0 :
            return 0
        

        backIndex = len(nums) - 1
        i = 0
        while i < backIndex:
            if nums[i] == val :
                while nums[backIndex] == val:
                    backIndex -= 1
                    if backIndex == i:
                        return backIndex if nums[backIndex] == val else backIndex + 1
                    
                nums[i] = nums[backIndex]
                nums[backIndex] = val
                backIndex -= 1
            i += 1
            
        
        return backIndex if nums[backIndex] == val else backIndex + 1  