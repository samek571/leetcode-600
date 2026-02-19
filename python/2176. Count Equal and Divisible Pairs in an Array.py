class Solution:
    def countPairs(self, nums, k):
        hsh = defaultdict(lambda: defaultdict(int))
        res = 0

        for i in range(len(nums)):
            ii = i % k

            if nums[i] in hsh:
                for mod_j, count in hsh[nums[i]].items():
                    if (ii * mod_j) % k == 0:
                        res += count

            hsh[nums[i]][ii] += 1

        return res
