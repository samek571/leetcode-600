class Solution:
    def maxSideLength(self, matrix: List[List[int]], threshold: int) -> int:
        m,n = len(matrix), len(matrix[0])
        prf = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                prf[i][j] = (matrix[i-1][j-1] + prf[i-1][j] + prf[i][j-1] - prf[i-1][j-1])

        res = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                length = res + 1
                if i >= length and j >= length:
                    r1, c1 = i-length + 1, j-length + 1

                    tmp = (prf[i][j] - prf[r1-1][j] - prf[i][c1-1] + prf[r1-1][c1-1])

                    if tmp <= threshold:
                        res += 1

        return res
