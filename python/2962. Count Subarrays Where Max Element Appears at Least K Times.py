class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        freq = defaultdict(int)
        res = 0
        for num in nums:
            freq[num] += 1
            while freq[max_val] >= k:
                freq[nums[left]] -= 1
                left += 1
            res += left
        return res
