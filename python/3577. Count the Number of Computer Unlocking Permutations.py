class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        return complexity[0] < min(complexity[1:]) and factorial(len(complexity)-1)%(10**9+7) or 0
