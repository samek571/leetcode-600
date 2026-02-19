class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:

        pf, res = 1, 0
        for p1, p2 in pairwise(prices):
            if p2 == p1 - 1:
                pf += 1
            else:
                res+= pf*(pf+1)//2
                pf = 1

        res += pf*(pf+1)//2

        return  res
