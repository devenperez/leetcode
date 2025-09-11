class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        # Subproblem: only nums 0 to i exist and i is always robbed
        dp = [0] * len(nums)

        for i, money in enumerate(nums):
            if i == 0 or i == 1:
                dp[i] = nums[i]
                continue

            if i == 2:
                dp[i] = nums[i] + dp[i - 2]
                continue

            dp[i] = nums[i] + max(dp[i - 2], dp[i - 3])

        return max(dp[-1], dp[-2])
        