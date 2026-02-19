class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:

        res, n = -float('inf'), len(nums)
        for i in range(n):
            res = max(res, abs(nums[i%n] - nums[(i+1)%n]))

        return res
