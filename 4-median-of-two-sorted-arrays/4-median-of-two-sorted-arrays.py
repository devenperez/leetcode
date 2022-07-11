class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        # Variables
        totalLength = len(nums1) + len(nums2)
        goalIndex = (totalLength / 2.0) - 0.5   # Index of median
        num1Index = 0
        num2Index = 0
        median = 0.0
        
        # Go through arrays simultaniously 
        # Indexing up only on the lower number
        # Stop after we hit "goalIndex"
        for i in range(int(goalIndex + 1.5)):
            # OOB Checks
            if num1Index >= len(nums1):
                lowestNum2 = nums2[num2Index]
                lowestNum1 = lowestNum2 + 1
            elif num2Index >= len(nums2):
                lowestNum1 = nums1[num1Index]
                lowestNum2 = lowestNum1 + 1
            else:
                
            # QOL variables
                lowestNum1 = nums1[num1Index]
                lowestNum2 = nums2[num2Index]
            
            # Index up logic
            if lowestNum1 <= lowestNum2:
                num1Index += 1
                if i == int(goalIndex) or i == round(goalIndex):
                    median += lowestNum1
            else:
                num2Index += 1
                if i == int(goalIndex) or i == round(goalIndex):
                    median += lowestNum2
        
        # Divide median by 2 if array is even
        if int(goalIndex) != round(goalIndex):
            median /= 2
        
        return median