class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], start_idx: int, k: int) -> int:
        n = 2 * 100000 + 1
        pref_arr = [0] * n

        for pos, quantity in fruits:
            pref_arr[pos] = quantity

        for i in range(1, n):
            pref_arr[i] += pref_arr[i - 1]

        res = 0
        #right
        for i in range(start_idx, min(start_idx + k, n - 1) + 1):
            r = i
            x = i - start_idx
            l = start_idx - (k - 2 * x)
            l = min(l, start_idx)
            _sum = pref_arr[r]
            if l > 0:
                _sum -= pref_arr[l - 1]
            res = max(res, _sum)

        #left
        for i in range(start_idx, max(start_idx - k, 0) - 1, -1):
            l = i
            x = start_idx - i
            r = start_idx + (k - 2 * x)
            r = max(min(n - 1, r), start_idx)
            _sum = pref_arr[r]
            if l > 0:
                _sum -= pref_arr[l - 1]
            res = max(res, _sum)

        return res
