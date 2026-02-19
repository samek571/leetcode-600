class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:

        def _helper(dp, coeff):
            for _ in range(n - 1):
                for i in range(len(dp)):
                    tmp = 0
                    for j, c in enumerate(coeff[i]):
                        idx = -1 if j >= i else -2
                        tmp += c*dp[j][idx]
                    dp[i].append(tmp)

            return sum(e[-1] for e in dp) % (10**9+7)


        if m == 1:
            return _helper([[3]], [[2]])
        if m == 2:
            return _helper([[6]], [[3]])
        elif m == 3:
            return _helper([[6], [6]], [[3,2], [2,2]])
        elif m == 4:
            return _helper([[6], [6], [6], [6]], [[3,1,2,2], [1,2,1,1], [2,1,2,2], [2,1,2,2]])
        else:
            return _helper(
                [[6], [6], [6], [6], [6], [6], [6], [6]],
                [[2,1,1,1,2,2,1,1],
                    [1,2,1,1,0,0,1,0],
                    [1,1,2,1,1,1,1,1],
                    [1,1,1,2,2,2,1,1],
                    [2,0,1,2,3,2,1,2],
                    [2,0,1,2,2,2,1,2],
                    [1,1,1,1,1,1,2,1],
                    [1,0,1,1,2,2,1,2]])
