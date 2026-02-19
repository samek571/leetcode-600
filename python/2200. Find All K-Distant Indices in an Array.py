class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:

        return [idx for idx in range(len(nums)) if key in nums[max(0,idx-k):idx+k+1]]
