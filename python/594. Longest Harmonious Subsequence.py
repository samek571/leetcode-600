class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hsh, res = Counter(nums), 0

        for num in hsh:
            new_num = num +1
            if new_num in hsh:
                current_length = hsh[num] + hsh[new_num]
                res = max(res, current_length)

        return res
