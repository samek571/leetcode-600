class Solution:
    def countValidSelections(self, nums: List[int]) -> int:

        right_sum, left_sum, res = sum(nums),0,0
        for i in range(len(nums)):
            if nums[i] == 0:
                if right_sum == left_sum:
                    res += 2
                    continue

                if right_sum - 1 == left_sum or right_sum + 1 == left_sum:
                    res += 1
                    continue
            else:
                right_sum, left_sum = right_sum - nums[i], left_sum + nums[i]


            if right_sum - left_sum < -2:
                return res

        return res
