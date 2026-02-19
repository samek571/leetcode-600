class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1

        s = 10
        for i in range(2, n + 1):
            tmp = 9
            cnt = 10
            for j in range(1, i):
                tmp *= cnt - 1
                cnt -= 1
            s += tmp
        return s
