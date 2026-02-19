class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for a in range(max(0, n - 2 * limit), min(limit, n) + 1):
            b = min(limit, n - a) - max(0, n - a - limit) + 1
            res += max(0, b)
        return res
