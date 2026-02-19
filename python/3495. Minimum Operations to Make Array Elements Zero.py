class Solution:
    def minOperations(self, queries: list[list[int]]) -> int:
        res = 0
        for a, b in queries:

            l,r, tmp_sum = 0,0,0
            k1, k2 = a, b
            while k1 != 0:
                k1 //= 4
                l += 1
            while k2 != 0:
                k2 //= 4
                r += 1

            tmp_sum += min((b - a + 1), (int(math.pow(4, l)) - a)) * l

            if r != l:
                tmp_sum += (b - int(math.pow(4, r - 1)) + 1) * r

            if r - l > 1:
                for j in range(l + 1, r):
                    tmp_sum += (int(math.pow(4, j)) - int(math.pow(4, j - 1))) * j

            res += tmp_sum // 2 if tmp_sum % 2 ==0 else 1+ tmp_sum // 2

        return res
