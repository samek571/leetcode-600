class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        _tpl_idx = [(num, i) for i, num in enumerate(nums)]
        _tpl_idx.sort(key=lambda x: -x[0])

        return [num for num, _ in sorted(_tpl_idx[:k], key=lambda x: x[1])]
