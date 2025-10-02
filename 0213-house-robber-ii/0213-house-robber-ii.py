class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) - 1
        dp = [0] * n    # Best of first i houses
        dp2 = [0] * n   # Best of first i houses without robbing the first one


        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        if n >= 1:
            dp[0] = nums[0]
            dp2[0] = 0
        if n >= 2:
            dp[1] = max(nums[0], nums[1])
            dp2[1] = nums[1]
        if n >= 3:
            dp[2] = max(nums[0] + nums[2], nums[1])
            dp2[2] = max(nums[1], nums[2])
        if n >= 4:
            dp[3] = max(nums[3] + dp2[1], nums[2] + dp2[0])
            dp2[3] = max(nums[1] + nums[3], nums[2])


        for i in range(3, n):
            dp[i] = max(nums[i] + dp[i - 2], nums[i - 1] + dp[i - 3])
            dp2[i] = max(nums[i] + dp2[i - 2], nums[i - 1] + dp2[i - 3])

        return max(dp[-1], dp2[-2] + nums[-1])