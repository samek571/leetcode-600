class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, n, groups = 0, len(nums), 0
        while i < n:
            limit = nums[i] + k
            i = bisect_right(nums, limit, i, n)
            groups += 1
        return groups
