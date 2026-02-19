class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        hsh = {}

        def dfs(i, last):
            if i == len(nums): return []
            if (i, last) in hsh: return hsh[(i, last)]

            res = dfs(i+1, last)

            if last == 1 or nums[i] % last == 0:
                tmp = [nums[i]] + dfs(i + 1, nums[i])
                if len(tmp) > len(res):
                    res = tmp

            hsh[(i, last)] = res


            return res


        return dfs(0, 1)
