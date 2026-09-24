# https://youtu.be/H9bfqozjoqs?si=vUJfA4wE3bLh83j1

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount+1):
            for coin in coins:
                if a - coin>=0:
                    dp[a] = min(dp[a], 1 + dp[a-coin])
        
        return int(dp[amount]) if dp[amount]!=float('inf') else -1