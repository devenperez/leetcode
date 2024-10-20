class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [-1] * len(nums)
        dp[0] = nums[0]

        if dp[0] == 0 and len(nums) > 1:
            return False

        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] - 1, nums[i])

            if dp[i] == 0 and i + 1 != len(nums):
                return False

        return True