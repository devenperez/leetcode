class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = [nums[0]]
        for i in range(1, len(nums)):
            sum.append(sum[i-1] + nums[i])
        return sum