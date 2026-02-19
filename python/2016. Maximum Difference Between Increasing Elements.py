class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        #tuple of (val, idx)
        stack,res = [], -1

        for idx, num in enumerate(nums):
            if not stack or (num < stack[-1][0]):
                stack.append((num, idx))

            if stack and (stack[-1][1] < idx and num > stack[-1][0]):
                res = max(res, num - stack[-1][0])

        return res
