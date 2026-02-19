class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:

        res = []
        for num in nums:
            flg = False
            for i in range(num):
                if i | (i + 1) == num:
                    res.append(i)
                    flg = True
                    break

            if not flg:
                res.append(-1)

        return res
