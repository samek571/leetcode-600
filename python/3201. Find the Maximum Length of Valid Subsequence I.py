class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even = [0, 0]
        odd = [0, 0]

        for x in nums:
            parity = x & 1
            even[parity] += 1
            odd[parity] = odd[parity ^ 1] + 1

        return max(max(even), max(odd))
