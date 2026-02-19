class Solution:
    def maxDifference(self, s: str) -> int:
        hsh = Counter(s)
        max_odd, min_even = 0, 100

        for ch in ascii_lowercase:
            if hsh[ch] % 2:
                max_odd = max(max_odd, hsh[ch])
            elif hsh[ch]:
                min_even = min(min_even, hsh[ch])

        return max_odd - min_even
