class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD, N = (10**9+7), 26
        v = [0] * N
        for ch in s:
            v[ord(ch) - 97] += 1

        M = [[0] * N for _ in range(N)]
        for j, step in enumerate(nums):
            q, r = divmod(step, N)
            for i in range(N):
                M[i][j] = q
            for k in range(1, r + 1):
                M[(j + k) % N][j] += 1

        def mat_mul(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
            res = [[0] * N for _ in range(N)]
            for i in range(N):
                ai = a[i]
                ri = res[i]
                for k, aik in enumerate(ai):
                    if aik:
                        bk = b[k]
                        for j in range(N):
                            ri[j] = (ri[j] + aik * bk[j]) % MOD
            return res

        def mat_vec(m: List[List[int]], vec: List[int]) -> List[int]:
            return [sum(mi[k] * vec[k] for k in range(N)) % MOD for mi in m]

        while t:
            if t & 1:
                v = mat_vec(M, v)
            M = mat_mul(M, M)
            t >>= 1

        return sum(v) % MOD
