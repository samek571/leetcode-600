class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        _sum, res, max_bits = 0,0,k.bit_length()

        for i in range(len(s)):
            bit = s[-1 - i]
            if bit == '1':
                if i < max_bits and _sum + (1 << i) <= k:
                    _sum += 1 << i #== //2
                    res += 1
            #otherwise leading zeroes skip
            else:
                res += 1

        return res
