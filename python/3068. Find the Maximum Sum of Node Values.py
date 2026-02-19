class Solution:
    def maximumValueSum(self, n: List[int], k: int, edges: List[List[int]]) -> int:
        s, c, d = 0, 0, float('inf')
        for x in n:
            s += max(x, x ^ k)
            if (x ^ k) > x:
                c ^= 1
            d = min(d, abs((x ^ k) - x))

        return s - d * c
