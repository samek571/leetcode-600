class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res = 0
        for v in nums:
            res |= v

        seen = {0: 1}
        for val in nums:
            for prev_or, cnt in list(seen.items()):
                new_or = prev_or | val
                tmp = seen[new_or] if new_or in seen else 0
                seen[new_or] = tmp + cnt

        return seen[res] if res in seen else 0
