class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        ps = list(accumulate(nums, initial=0))
        dp = [-inf] * (len(nums)+1)

        for idx in range(k, len(nums)+1):
            dp[idx] = max(0, dp[idx-k]) + ps[idx] - ps[idx-k]

        return max(dp)
