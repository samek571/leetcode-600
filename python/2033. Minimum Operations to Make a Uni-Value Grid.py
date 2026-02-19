class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        n, res = len(grid) * len(grid[0]), 0
		med = sorted([c for r in grid for c in r])[n // 2]

		for r in grid:
            for c in r:
                res += abs(med - c) // x

                if abs(med - c) % x != 0:
                    return -1

        return res
