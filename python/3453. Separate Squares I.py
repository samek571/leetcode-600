class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        low, high = 1e18, -1e18

        for x, y, l in squares:
            low = min(low, float(y))
            high = max(high, float(y + l))

        for _ in range(100):
            mid = (low + high) / 2.0
            a, b= 0.0, 0.0

            for x, y, l in squares:
                bottom = y
                top = y + l

                if mid <= bottom:
                    a += l * l
                elif mid >= top:
                    b += l * l
                else:
                    a += (top - mid) * l
                    b += (mid - bottom) * l

            if a > b:
                low = mid
            else:
                high = mid

        return low
