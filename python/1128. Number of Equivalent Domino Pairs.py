class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        return sum(val*(val-1)//2 for val in Counter([tuple(sorted(set(dom))) for dom in dominoes]).values())
