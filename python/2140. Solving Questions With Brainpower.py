class Solution:
    def mostPoints(self, q: List[List[int]]) -> int:
        n = len(q)
        dp = [0] * (n+1)

        for i in range(n-1, -1, -1):
            next_q = min(n, i+q[i][1]+1)

            dp[i] = max(dp[i+1], q[i][0]+dp[next_q])

        return dp[0]
