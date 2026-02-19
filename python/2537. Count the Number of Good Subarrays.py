class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        hsh = defaultdict(int)
        res = i = j = cnt = 0
        n = len(nums)

        while i < n:
            while j < n and cnt < k:
                hsh[nums[j]] += 1
                cnt += hsh[nums[j]] - 1
                j += 1

            if cnt < k:
                break

            res += n - j + 1

            hsh[nums[i]] -= 1
            cnt -= hsh[nums[i]]
            i += 1

        return res
