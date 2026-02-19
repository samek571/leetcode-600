class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[-1 for _ in range(n)] for _ in range(m)]

        for guard in guards:
            grid[guard[0]][guard[1]] = "g"

        for wall in walls:
            grid[wall[0]][wall[1]] = "w"

        for guard in guards:

            # left
            idx = guard[0]
            jdx = guard[1] - 1
            while(jdx >= 0 and grid[idx][jdx] not in ["g", "w"]):
                grid[idx][jdx] = True
                jdx -= 1

            # up
            idx = guard[0] - 1
            jdx = guard[1]
            while(idx >= 0 and grid[idx][jdx] not in ["g", "w"]):
                grid[idx][jdx] = True
                idx -= 1

            # right
            idx = guard[0]
            jdx = guard[1] + 1
            while(jdx < n and grid[idx][jdx] not in ["g", "w"]):
                grid[idx][jdx] = True
                jdx += 1

            # down
            idx = guard[0] + 1
            jdx = guard[1]
            while(idx < m and grid[idx][jdx] not in ["g", "w"]):
                grid[idx][jdx] = True
                idx += 1

        res = 0
        for row in grid:
            res += row.count(-1)

        return res
