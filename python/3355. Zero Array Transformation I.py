class Solution:
    #its way nicer than doing the prefix tree
    def isZeroArray(self, nums: List[int], q: List[List[int]]) -> bool:
        _lst = [0]*(len(nums)+1)
        for l,r in q:
            _lst[l] += 1
            _lst[r+1] -= 1

        return all(map(le, nums, accumulate(_lst)))
