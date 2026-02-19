class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        res, this, const_max_val = 0, 0, max(nums)
        for elem in nums:
            if elem == const_max_val:
                this += 1
                res = max(res, this)
            else:
                this = 0

        return res
