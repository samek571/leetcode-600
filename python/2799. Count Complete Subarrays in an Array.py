class Solution:
    def countCompleteSubarrays(self, nums):

        total_unique, n = len(set(nums)), len(nums)
        hsh = defaultdict(int)
        unique_count, res, r = 0, 0, 0

        for l in range(n):
            while r < n and unique_count < total_unique:
                if hsh[nums[r]] == 0:
                    unique_count += 1
                hsh[nums[r]] += 1
                r += 1

            if unique_count == total_unique:
                res += (n - r + 1)

            hsh[nums[l]] -= 1
            if hsh[nums[l]] == 0:
                unique_count -= 1

        return res
