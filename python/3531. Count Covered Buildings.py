class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:

        hshx, hshy = {}, {} #no need for default dic

        for x, y in buildings:
            for i, j, hsh in ((x, y, hshx), (y, x, hshy)): #fancy trick instead of 2 forloops
                if i not in hsh:
                    hsh[i] = [j, j]
                else:
                    hsh[i][0] = min(hsh[i][0], j)
                    hsh[i][1] = max(hsh[i][1], j)

        res = 0
        for x, y in buildings:
            preX, postX = hshx[x]
            preY, postY = hshy[y]
            if preX < y < postX and preY < x < postY:
                res += 1

        return res
