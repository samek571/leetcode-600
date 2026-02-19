class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [1] + [0] * n
        p = 1 if 0 < k else 0

        for i in range(1, n + 1):
            dp[i] = p / maxPts

            if i < k: p += dp[i]
            if 0 <= i - maxPts and i - maxPts < k: p -= dp[i - maxPts]

        return sum(dp[k:])
