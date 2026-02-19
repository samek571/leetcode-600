class Solution:
    def isBeautiful(self, num: int) -> bool:
        freq = [0] * 10
        tmp = num
        while tmp > 0:
            freq[tmp % 10] += 1
            tmp //= 10

        for digit in range(10):
            if freq[digit] != 0 and freq[digit] != digit:
                return False

        return True

    def nextBeautifulNumber(self, n: int) -> int:
        idx = n + 1
        while not self.isBeautiful(idx):
            idx += 1
        return idx
