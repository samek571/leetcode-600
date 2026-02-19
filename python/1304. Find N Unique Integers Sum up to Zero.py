class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [(n*(n+1)//2) -1] + [-i for i in range(2, n+1)]
