
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        #return (sum(collections.Counter(nums).keys()) - len(nums))
        #return -len(set(nums)) + len(nums)

        last = {}
        res = 0

        for i, num in enumerate(nums):
            if num in last and last[num] >= 3 * res:
                res = math.ceil((last[num] + 1) / 3)
            last[num] = i

        return res
