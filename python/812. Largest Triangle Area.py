class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n, res =len(points), 0
        for i in range(n-2):
            x0, y0=points[i]

            for j in range(i+1, n-1):
                x1, y1=points[j]
                for k in range(j+1, n):
                    c0, c1=points[k]
                    area=(x1-x0)*(c1-y0) - (y1-y0)*(c0-x0)
                    res=max(res, abs(area))
        return res/2
