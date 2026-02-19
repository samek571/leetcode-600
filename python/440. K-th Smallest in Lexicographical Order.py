class Solution:
    def _helpr(self, count: int, next: int, n: int) -> int:
        count_num = 0
        while count <= n:
            count_num += min(n + 1, next) - count
            count *= 10
            next *= 10
        return count_num

    def findKthNumber(self, n: int, k: int) -> int:
        res = 1
        k -= 1

        while k > 0:
            count = self._helpr(res, res + 1, n)
            if count <= k:
                res += 1
                k -= count
            else:
                res *= 10
                k -= 1
        return res
