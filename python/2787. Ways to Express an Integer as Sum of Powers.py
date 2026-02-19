class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        powers = []
        idx = 1
        while True:
            _power = pow(idx, x)
            if _power > n:
                break
            powers.append(_power)
            idx += 1

        dp = [0] * (n + 1)
        dp[0] = 1
        for _power in powers:
            for s in range(n, _power - 1, -1):
                dp[s] = (dp[s] + dp[s - _power]) % (10**9+7)

        return dp[n]
