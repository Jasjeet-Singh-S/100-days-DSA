class Solution:
    def knapsack(self, W, values, weights):
        n = len(weights)
        # dp[i][c] = best value using the first i items with capacity c
        dp = [[0] * (W + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            w = weights[i - 1]
            v = values[i - 1]
            for c in range(W + 1):
                # Option 1: skip item i
                dp[i][c] = dp[i - 1][c]
                # Option 2: take item i, if it fits
                if w <= c:
                    dp[i][c] = max(dp[i][c], dp[i - 1][c - w] + v)

        return dp[n][W]

# ask claude honestly, i didnt understand striver vid
# i honestly dont understand this ngl
# im gonna move on lowkey