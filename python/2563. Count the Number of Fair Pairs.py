class Solution:
    def countFairPairs(self, nums: List[int], l: int, u: int) -> int:
        nums.sort()

        def count(x):
            ct = 0
            i = 0
            for j in range(1, len(nums)):
                while i < j and nums[i] + nums[j] < x:
                    i += 1
                while i > 0 and nums[i - 1] + nums[j] >= x:
                    i -= 1
                ct += j - i
            return ct

        return count(l) - count(u + 1)
