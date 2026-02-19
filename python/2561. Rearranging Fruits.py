class Solution:
    def minCost(self, b1, b2):
        hsh1 = Counter(b1)
        hsh2 = Counter(b2)
        all_keys = set(hsh1.keys()) | set(hsh2.keys())
        min_val = min(min(b1), min(b2))

        diff = []
        for key in all_keys:
            total = hsh1.get(key, 0) - hsh2.get(key, 0)
            if total % 2 != 0:
                return -1
            if total > 0:
                diff.extend([key] * (total // 2))

        surplus = []
        for key in all_keys:
            total = hsh2.get(key, 0) - hsh1.get(key, 0)
            if total % 2 != 0:
                return -1
            if total > 0:
                surplus.extend([key] * (total // 2))

        diff.sort()
        surplus.sort(reverse=True)

        res = 0
        for i in range(len(diff)):
            res += min(diff[i], 2 * min_val, surplus[i])

        return res
