class Solution:
    #lazy eval
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        def comb(x, y):
            return precomputed_f[x] * _helpr[y] % mod * _helpr[x - y] % mod if (0 <= y <= x) else 0

        if k>n-1: return 0

        mod=10**9+7
        precomputed_f = [1]*n
        for i in range(1, n):
            precomputed_f[i] = precomputed_f[i-1]*i %mod

        _helpr = [1] * n
        _helpr[n-1] = pow(precomputed_f[n-1], mod-2, mod)
        for i in range(n-1, 0, -1):
            _helpr[i-1] = _helpr[i]*i %mod

        return m*comb(n-1, k) %mod *pow(m-1, n-1-k, mod) %mod
