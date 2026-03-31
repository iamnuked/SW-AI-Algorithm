# https://leetcode.com/problems/triangle/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = []
        level = len(triangle)
        for i in range(level):
            dp.append([0] * (i+1))

        print(dp)
        dp[0][0] = triangle[0][0]
        for i in range(1, level):
            for n in range(len(triangle[i])):
                if n == 0:
                    dp[i][n] = dp[i-1][n] + triangle[i][n]
                elif n == i:
                    dp[i][n] = dp[i-1][n-1] + triangle[i][n]
                else:
                    dp[i][n] = min(dp[i-1][n-1], dp[i-1][n]) + triangle[i][n]


        return min(dp[-1])
