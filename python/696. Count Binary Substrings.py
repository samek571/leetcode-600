class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        runs = [len(m.group(0)) for m in re.finditer(r'0+|1+', s)]
        return sum(min(a, b) for a, b in zip(runs, runs[1:]))
