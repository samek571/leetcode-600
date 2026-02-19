class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        collected = Counter(nums)
        maxFreq = max(collected.values())
        return sum(freq for freq in collected.values() if freq == maxFreq)
