class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        #we take a max out of the list of all possible combinations,
        #keep in mind the outter max is bounded by 0
        return max( max((x-y)*z for x,y,z in combinations(nums,3)) , 0)
