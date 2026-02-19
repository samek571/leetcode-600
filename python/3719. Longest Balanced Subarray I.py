class Solution:
    def longestBalanced(self, nums: List[int]) -> int:

        res, n = 0, len(nums)
        for idx in range(n):
            odd, even = set(), set()

            for jdx in range(idx, n):
                num = nums[jdx]
                if num%2 == 1:
                    odd.add(num)
                else:
                    even.add(num)
                if len(odd) == len(even):
                    res = max(res, jdx-idx+1)

        return res
