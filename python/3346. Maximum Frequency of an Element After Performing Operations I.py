class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        maxVal = max(nums) + k + 2
        cnt = [0] * maxVal

        for v in nums:
            cnt[v] += 1

        for i in range(1, maxVal):
            cnt[i] += cnt[i - 1]

        res = 0
        for i in range(maxVal):
            left = max(0, i - k)
            right = min(maxVal - 1, i + k)
            total = cnt[right] - (cnt[left - 1] if left else 0)
            freq = cnt[i] - (cnt[i - 1] if i else 0)
            res = max(res, freq + min(numOperations, total - freq))

        return res
