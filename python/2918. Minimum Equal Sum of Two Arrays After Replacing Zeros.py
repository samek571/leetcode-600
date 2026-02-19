class Solution(object):
    def minSum(self, nums1, nums2):
        tmp1 = sum(1 for x in nums1 if x == 0)
        tmp2 = sum(1 for x in nums2 if x == 0)
        s1 = tmp1 + sum(nums1)
        s2 = tmp2 + sum(nums2)

        if (s2 > s1 and tmp1 == 0) or (s2 < s1 and tmp2 == 0): return -1

        return max(s1, s2)
