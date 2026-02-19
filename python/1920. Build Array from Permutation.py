class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n

        #since permutation is a bijection
        for i in range(n):
            res[i] = nums[nums[i]]

        return res
