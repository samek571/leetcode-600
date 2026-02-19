from functools import lru_cache
from math import comb

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        mod = 10**9 + 7
        cnt = [0] * 10
        _sum = 0

        for c in num:
            d = int(c)
            cnt[d] += 1
            _sum += d

        #not possible...
        if _sum % 2 != 0: return 0

        n = len(num)
        m = n // 2 + 1
        target_sum = _sum // 2

        #precomputing binomial coefficients  
        c = [[0] * (m + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            c[i][0] = 1
            for j in range(1, i + 1):
                c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % mod
        
        
        #caching
        @lru_cache(maxsize=None)
        def dfs(i, rest_sum, a, b):
            if i > 9: return int(rest_sum == 0 and a == 0 and b == 0)
            if a == 0 and rest_sum != 0: return 0

            _res = 0
            for l in range(min(cnt[i], a) + 1):
                r = cnt[i] - l
                if 0 <= r <= b and l * i <= rest_sum:
                    ways = c[a][l] * c[b][r] % mod
                    _again = dfs(i + 1, rest_sum - l * i, a - l, b - r)
                    _res = (_res + ways*_again % mod) % mod

            return _res

        return dfs(0, target_sum, n // 2, (n + 1) // 2)
