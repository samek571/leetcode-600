class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:

        side = 0
        for idx in range(len(bottomLeft)):
            for jdx in range(idx + 1, len(bottomLeft)):
                minX = max(bottomLeft[idx][0], bottomLeft[jdx][0])
                minY = max(bottomLeft[idx][1], bottomLeft[jdx][1])
                maxX = min(topRight[idx][0], topRight[jdx][0])
                maxY = min(topRight[idx][1], topRight[jdx][1])

                if minX < maxX and minY < maxY:
                    length = min(maxX - minX, maxY - minY)
                    side = max(side, length)

        return side*side
