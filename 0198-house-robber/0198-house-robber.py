class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) < 3:
            return max(nums)

        # Subproblem: only nums 0 to i exist and i is always robbed
        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[2] + nums[0]


        for i in range(3, len(nums)):
            dp[i] = nums[i] + max(dp[i - 2], dp[i - 3])

        return max(dp[-1], dp[-2])
        