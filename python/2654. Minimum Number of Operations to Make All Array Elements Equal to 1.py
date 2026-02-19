class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n,val,_gcd = len(nums),0,0

        for x in nums:
            if x == 1:
                val += 1
            _gcd = gcd(_gcd, x)

        if val > 0: return n - val
        if _gcd > 1: return -1

        min_len = n
        for i in range(n):
            _gcd = 0
            for j in range(i, n):
                _gcd = gcd(_gcd, nums[j])
                if _gcd == 1:
                    min_len = min(min_len, j - i + 1)
                    break

        return min_len + n - 2
