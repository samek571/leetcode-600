class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        rem = [0] * value
        for num in nums:
            rem[num % value] += 1

        res = 0
        while rem[res % value]:
            rem[res % value] -= 1
            res += 1
        return res
