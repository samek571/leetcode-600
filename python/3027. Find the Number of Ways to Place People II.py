class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (p[0],-p[1]))

        res = 0
        for idx, (_,y1) in enumerate(points):
            min_y = -inf
            for _, y2 in points[idx+1: ]:
                if min_y < y2 <= y1:
                    res += 1
                    min_y = y2

        return res
