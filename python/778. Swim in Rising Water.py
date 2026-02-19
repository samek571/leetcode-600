class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        seen = [[0] * n for _ in range(n)]
        pq = [(grid[0][0], 0, 0)]
        res = 0
        directions = [0, 1, 0, -1, 0]
        while pq:

            h, x, y = heapq.heappop(pq)
            res = max(res, h)
            if x == n - 1 and y == n - 1: return res
            if seen[x][y]: continue

            seen[x][y] = 1

            for k in range(4):
                dx, dy = x + directions[k], y + directions[k + 1]
                if 0 <= dx < n and 0 <= dy < n and not seen[dx][dy]:
                    heapq.heappush(pq, (grid[dx][dy], dx, dy))

        return res
