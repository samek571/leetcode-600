class Solution:
    def subsetXORSum(self, n: List[int], sum=0) -> int:
        for i in n:
            sum |= i

        return sum * pow(2, len(n)-1)
