class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        if len(s) <= 2:
            return 0

        alphabet, res = set(s), 0
        for c in alphabet:

            l, r = s.find(c), s.rfind(c)
            if l != r:
                res += len(set(s[l + 1 : r]))

        return res
