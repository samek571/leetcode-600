class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = collections.defaultdict(int)
        for i in nums:
            if i < k:
                return -1
            elif i > k:
                mpp[i] += 1

        return len(res)
