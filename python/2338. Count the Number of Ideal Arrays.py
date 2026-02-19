class Solution:
    #eratosthenes seeve something i knew since highschool
    def idealArrays(self, n: int, maxValue: int) -> int:
        primes = []
        res = 1
        for num in range(2, maxValue + 1):
            cur = 1

            for p in primes:
                if num == 1:
                    break

                k = 0
                while num % p == 0:
                    num //= p
                    k += 1
                    cur = cur * (n + k - 1) // k

            if num != 1:
                primes.append(num)
                cur = cur * n

            res = (res + cur) % (10**9 + 7)
        return res
