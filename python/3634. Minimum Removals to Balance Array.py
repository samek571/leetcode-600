class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        idx, window, n = 0, 0, len(nums)

        for jdx in range(n):

            while nums[jdx] > nums[idx] * k:
                idx += 1
            window = max(window, jdx - idx + 1)

        return n - window
