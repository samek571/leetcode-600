class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        res, last = 0, float('-inf')

        for num in nums:
            if max(num - k, last + 1) <= num + k:
                last, res  = max(num - k, last + 1), res +1

        return res
