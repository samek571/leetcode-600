class Solution:
    def minDeletionSize(self, s: List[str]) -> int:
        n, m = len(s), len(s[0])
        dp = [1] * m

        for i in range(m):
            for j in range(i):
                for k in range(n):
                    if s[k][j] > s[k][i]:
                        break
                else:
                    dp[i] = max(dp[i], dp[j] + 1)

        return m - max(dp)
