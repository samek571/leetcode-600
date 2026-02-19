class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def _helpr(nums1, nums2, target) -> int:
            count = 0
            for a in nums1:
                if a > 0:
                    l, r = 0, len(nums2)-1
                    while l <= r:
                        mid = (l + r) // 2
                        if a * nums2[mid] <= target:
                            l = mid + 1
                        else:
                            r = mid - 1
                    count += l
                elif a < 0:
                    l, r = 0, len(nums2)-1
                    while l <= r:
                        mid = (l + r) // 2
                        if a * nums2[mid] <= target:
                            r = mid - 1
                        else:
                            l = mid + 1
                    count += len(nums2) - l
                else:
                    if target >= 0:
                        count += len(nums2)
            return count


        nums2.sort()
        res, upper = -10**11-1, 10**11+1 #constraints are 10**5 but its result might be twice that
        while res < upper:
            mid = (res + upper) // 2
            if _helpr(nums1, nums2, mid) < k:
                res = mid + 1
            else:
                upper = mid

        return res
