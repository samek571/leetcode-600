class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:

        res = 0
        while len(nums) > 1:
            inv = 0
            _idxtmp = 0
            _sumtmp = nums[0] + nums[1]

            for i in range(len(nums) - 1):
                inv |= nums[i] > nums[i + 1]
                s = nums[i] + nums[i + 1]
                if s < _sumtmp:
                    _sumtmp = s
                    _idxtmp = i

            if not inv:
                return res

            nums[_idxtmp] += nums[_idxtmp + 1]
            nums.pop(_idxtmp + 1)
            res += 1

        return res
