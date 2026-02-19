class Solution:
    def maxDiff(self, n: int) -> int:
        word, digit, digit2 = str(n), -1, -1
        for ch in word:
            d = int(ch)
            if digit == -1 and d != 9:
                digit = d
            if digit2 == -1 and d > 1:
                digit2 = d

        y = 1 if (int(word[0]) == digit2) else 0

        tmp, maxi, mini, it = n, 0,0,0
        while tmp > 0:
            d = tmp % 10
            tmp //= 10

            if d == digit:
                maxi += 9 * (10 ** it)
            else:
                maxi += d * (10 ** it)

            if d == digit2:
                mini += y * (10 ** it)
            else:
                mini += d * (10 ** it)
            it += 1


        return maxi - mini
