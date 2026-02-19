class Solution:
    def countDays(self, days: int, m: List[List[int]]) -> int:
        m.sort(key=lambda x: x[0])
        res = m[0][0] - 1
        n = len(m)

        for i in range(1, n):
            if m[i][0] <= m[i - 1][1]:
                if m[i][1] < m[i - 1][1]:
                    m[i][1] = m[i - 1][1]
            else:
                res += m[i][0] - m[i - 1][1] - 1

        return res + days - m[n - 1][1]
