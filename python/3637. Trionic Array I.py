class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n, idx = len(nums), 0

        while idx + 1 < n and nums[idx] < nums[idx + 1]:
            idx += 1
        if idx == 0 or idx == n - 1:
            return False

        curr = idx
        while idx + 1 < n and nums[idx] > nums[idx + 1]:
            idx += 1
        if idx == curr or idx == n - 1:
            return False

        while idx + 1 < n and nums[idx] < nums[idx + 1]:
            idx += 1

        return idx == n - 1
