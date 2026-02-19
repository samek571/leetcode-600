class Solution:
    def maxFreqSum(self, s: str) -> int:
        hsh = collections.Counter(s)

        maxvow, maxnonvow = 0, 0
        for key, val in hsh.items():
            if key in {"a","e","i","o","u"}:
                maxvow = max(maxvow, val)
            else:
                maxnonvow = max(maxnonvow, val)

        return maxnonvow + maxvow
