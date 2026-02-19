class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        seen = set(nums)
        res = original

        while res <= 1000:
            if res in seen:
               res *= 2
            else:
                break

        return res
