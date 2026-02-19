class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:

        n, m = len(moveTime), len(moveTime[0])
        #heapified q as we are doing dijkstra sort of
        q = [(0, 0, 0)] #ordered triple of time, index i, index j
        seen = set((0, 0))
        res = 0
        while q:
            t, i, j = heapq.heappop(q)
            res = max(res, t) #we simply handle the waiting as this
            if i == n - 1 and j == m - 1: break #finish

            for dx, dy in [(-1, 0), (0,-1), (1,0), (0,1)]:
                x, y = i + dx, j + dy #new dir

                #within borders and new tile -- possible forward step weighted in heap by its excellence
                if (x, y) not in seen and 0 <= x < n and 0 <= y < m:
                    heapq.heappush(q, (max(res, moveTime[x][y]) + 1, x, y))
                    seen.add((x, y))

        return res
