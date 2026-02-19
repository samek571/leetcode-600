class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for i in range(low, high + 1):
            if i < 100:
                res += (i % 11 == 0)
            elif i > 1000:
                i0 = i % 10
                i1 = (i % 100) // 10
                i2 = (i % 1000) // 100
                i3 = i // 1000
                res += (i0 + i1 == i2 + i3)
        return res
