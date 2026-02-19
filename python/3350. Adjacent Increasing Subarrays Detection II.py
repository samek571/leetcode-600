class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        pre, res, acc = 0,0,1

        for idx in range(1, len(nums)):
            if nums[idx-1] < nums[idx]:
                acc += 1
            else:
                pre, acc = acc, 1
            res = max(res, acc // 2, min(pre, acc))

        return res
