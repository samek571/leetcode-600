class Solution:
    def minimumDeletions(self, s: str) -> int:
        b = res = 0
        for c in s:
            if c == 'b':
                b += 1
            else: # c == 'a'
                res = min(res + 1, b)
        return res
