# https://leetcode.com/problems/house-robber/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def rob(self, nums: List[int]) -> int:
        nums_len = len(nums)
        dp = [0] * 3
        dp[0] = nums[0]
        if nums_len == 1:
            return dp[0]

        dp[1] = max(nums[0], nums[1])
        if nums_len == 2:
            return dp[1]

        for n in range(2, nums_len):
            dp[n%3] = max(dp[(n-2)%3]+nums[n], dp[(n-1)%3])

        return dp[n%3]