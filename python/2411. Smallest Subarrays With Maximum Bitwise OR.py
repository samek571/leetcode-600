class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        for idx in range(len(nums)):
            tmp = nums[idx]
            for jdx in range(idx - 1, -1, -1):
                if (nums[jdx] | tmp) == nums[jdx]:
                    break
                nums[jdx] |= tmp
                res[jdx] = idx - jdx + 1

        return res
