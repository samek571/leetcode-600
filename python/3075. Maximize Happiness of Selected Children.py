class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        return sum(max(0, hdx - idx) for idx, hdx in enumerate(happiness[:k]))
