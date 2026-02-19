class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        n, l,r = len(arr), 0, 2
        if n < 3: return False
        while r<n:
            if (arr[l] % 2 != 0) & (arr[l + 1] % 2 != 0) & (arr[r] % 2 != 0): return True

            l,r = l+1, r+1

        return False
