#essentialy the same as 3341 problem but we track extra partiy because we could have gotten to particular xy position
# sooner and it might be different parity aswell as lowe price therefore
# its not sufficient to just do one pass and track x+ymod2
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:

        n, m = len(moveTime), len(moveTime[0])
        #heapified q as we are doing dijkstra sort of
        q = [(0, 0, 0, 0)] #ordered quad of time, parity, index i, index j
        seen = set() #i j parity

        while q:
            t, p, i, j = heapq.heappop(q)
            if (i, j, p) in seen: continue #we need totrack parity aswell
            seen.add((i, j, p))

            if i == n - 1 and j == m - 1: return t #exit branch

            for dx, dy in [(-1, 0), (0,-1), (1,0), (0,1)]:
                x, y = i + dx, j + dy #new dir

                #within borders and new tile -- possible forward step weighted in heap by its excellence
                if 0 <= x < n and 0 <= y < m:
                    arrive = max(t, moveTime[x][y]) + (1 if p == 0 else 2)
                    heapq.heappush(q, (arrive, 1-p, x, y))

        return -1
