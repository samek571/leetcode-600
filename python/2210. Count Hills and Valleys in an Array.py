class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        high = 0
        low = 0
        res = 0
        n = len(nums)

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                high = 1
                if low != 0:
                    res += 1
                    low = 0
            elif nums[i] < nums[i - 1]:
                low = 1
                if high != 0:
                    res += 1
                    high = 0

        return res
