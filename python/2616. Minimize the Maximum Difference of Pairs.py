class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n, l, r = len(nums), 0, nums[-1] - nums[0]


        while l < r:
            m, pairs = (r + l) // 2, 0
            idx = 1
            while idx < n:
                if nums[idx] - nums[idx-1] <= m:
                    pairs += 1
                    idx += 1
                idx += 1
            if pairs >= p:
                r = m
            else:
                l = m + 1
        return l
