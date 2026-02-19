class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        res, mod = 0, 10**9+7
        h1, h2 = defaultdict(int), defaultdict(int)

        for i in range(len(nums)):
            h1[nums[i]]+=1

        for idx in range(len(nums)):
            res += h2.get(nums[idx]*2,0) * (h1[2*nums[idx]] - h2[2*nums[idx]] - (1 if 2*nums[idx] == nums[idx] else 0))
            h2[nums[idx]] += 1

        return res%mod
