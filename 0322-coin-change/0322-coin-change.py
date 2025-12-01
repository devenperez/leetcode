class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Complexities:
        Time:  O(mn)
        Space: O(m)

        where n = len(coins), m = amount
        """

        dp = [-1] * (amount + 1)

        dp[0] = 0
        for i in range(amount + 1):
            for coinValue in coins:
                if dp[i] == -1 or i + coinValue > amount:
                    continue
                elif dp[i + coinValue] == -1:
                    dp[i + coinValue] = dp[i] + 1
                else:
                    dp[i + coinValue] = min(dp[i + coinValue], dp[i] + 1)

        print(dp)
        return dp[amount]
