class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()

        f, s = -1, -1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                if f==-1:
                    f=nums[i]
                else:
                    s=nums[i]
        return [f,s]
