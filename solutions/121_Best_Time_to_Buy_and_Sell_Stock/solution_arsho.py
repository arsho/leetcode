class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        if n<=1:
            return 0
        dp = [0 for i in range(n)]
        dp[1] = max(0, prices[1]-prices[0])
        min_value = min(prices[0], prices[1])
        for i in range(2, n):
            diff = prices[i] - min_value
            dp[i] = max(diff, dp[i-1])
            if prices[i] < min_value:
                min_value = prices[i]
        return dp[n-1]

