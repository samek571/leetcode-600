class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        arr = sorted(nums)
        freq = Counter(arr)

        best = 0
        for i, v in enumerate(arr):
            left = bisect_left(arr, v - k)
            right = bisect_right(arr, v + k)
            in_band = right - left

            keep_v = freq[v] + min(in_band - freq[v], numOperations)

            right2 = bisect_right(arr, v + 2 * k)
            change_all = min(right2 - i, numOperations)

            best = max(best, keep_v, change_all)

        return best
