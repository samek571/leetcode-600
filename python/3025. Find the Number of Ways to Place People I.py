class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(reverse=True)

        res = 0
        for idx in range(len(points)):
            x1, y1 = points[idx]
            for jdx in range(len(points)):
                if idx == jdx: continue

                x2, y2 = points[jdx]
                if x1 <= x2 and y1 >= y2 and (x1 < x2 or y1 > y2):

                    flag = True
                    for kdx in range(len(points)):
                        if kdx in {idx, jdx}: continue

                        x3, y3 = points[kdx]
                        if x1 <= x3 <= x2 and y1 >= y3 >= y2:
                            flag = False
                            break

                    if flag:
                        res += 1
        return res
