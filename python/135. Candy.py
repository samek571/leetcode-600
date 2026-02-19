class Solution:
    def candy(self, ratings: List[int]) -> int:
        n, res = len(ratings), [1 for _ in range(len(ratings))]

        for idx in range(1, n):
            if ratings[idx] > ratings[idx-1]:
                res[idx] = res[idx-1] + 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                res[i] = max(res[i], res[i+1] + 1)

        return sum(res)
