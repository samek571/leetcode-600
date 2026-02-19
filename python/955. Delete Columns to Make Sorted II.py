class Solution:
    def minDeletionSize(self, strs):
        n, m = len(strs), len(strs[0])
        sorted_pairs = [False] * (n - 1)
        res_idx = 0

        def aux(col: int, mode: int) -> bool:
            bad = False
            for i in range(n - 1):
                if sorted_pairs[i]:
                    continue
                if strs[i][col] > strs[i + 1][col]:
                    bad = True
                    if mode == 0:
                        return True
                elif strs[i][col] < strs[i + 1][col] and mode == 1:
                    sorted_pairs[i] = True
            return bad

        for col in range(m):
            if aux(col, 0):
                res_idx += 1
                continue

            aux(col, 1)

            if all(sorted_pairs):
                break

        return res_idx

