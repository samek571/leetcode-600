class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            root = int(math.isqrt(num))
            if root * root == num:
                continue

            cnt, tmp = 0, 0
            for i in range(1, root + 1):
                if num % i == 0:
                    cnt += 2
                    tmp += i + num // i
            if cnt == 4:
                res += tmp

        return res
