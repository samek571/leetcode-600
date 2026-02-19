class Solution:
    def minTimeToVisitAllPoints(self, coords: List[List[int]]) -> int:
        res = 0
        for idx in range(1, len(coords)):
            res += max(abs(coords[idx][0] - coords[idx-1][0]), abs(coords[idx][1] - coords[idx-1][1]))

        return res
