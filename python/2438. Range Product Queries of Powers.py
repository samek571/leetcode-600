class Solution:
    def productQueries(self, n: int, q: List[List[int]]) -> List[int]:

        powers = []
        while n:
            lowest = n & -n
            powers.append(lowest)
            n ^= lowest

        n = len(powers)
        seen = [[0] * n for _ in range(n)]
        for r, val in enumerate(powers):
            seen[r][r] = val
            for c in range(r + 1, n):
                seen[r][c] = (seen[r][c - 1] * powers[c] % (10**9+7))

        return [seen[i][j] for i, j in q]
