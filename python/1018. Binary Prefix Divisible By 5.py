class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res, cnt = [], 0

        for bit in nums:
            cnt = (2*cnt + bit) % 5
            res.append(cnt == 0)

        return res
