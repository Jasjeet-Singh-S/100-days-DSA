# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: list[int]) -> int:
        if nums==None:
            return None

        n = len(nums)
        if n==1:
            return nums[0]  # base case 1, self explanatory
        if n==2:
            return max(nums[0], nums[1])  # base case 2, also self explanatory
        if n==3:
            return max(nums[0]+nums[2], nums[1])  # base case 3, also self explanatory
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        dp[2] = max(nums[0]+nums[2], nums[1])  # the same thing we did in the base cases but a more general case to solve further

        for i in range(3, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])  # main dp relation. thoda dimaag laga ke samjh lo

        return dp[n-1]