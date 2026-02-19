class Solution:
    def kMirror(self, base: int, limit: int) -> int:

        def to_base(number):
            digits = ''
            while number: digits = str(number % base) + digits; number //= base
            return digits or '0'


        def palindromes():
            length = 1
            while True:
                half = (length + 1) // 2
                start = 10 ** (half - 1) if half > 1 else 1
                end = 10 ** half
                for prefix in range(start, end):
                    t = str(prefix)
                    yield int(t + (t[-2::-1] if length & 1 else t[::-1]))
                length += 1

        res, found = 0, 0
        for number in palindromes():
            repr_base = to_base(number)
            if repr_base == repr_base[::-1]:
                res += number
                found += 1
                if found == limit:
                    return res
