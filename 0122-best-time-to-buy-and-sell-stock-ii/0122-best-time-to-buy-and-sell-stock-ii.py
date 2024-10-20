class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            before = prices[i]
            after = prices[i + 1]

            if before < after:
                profit += after - before
            
        return profit
