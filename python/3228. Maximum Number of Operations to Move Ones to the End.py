class Solution:
    def maxOperations(self, s: str) -> int:

        res, limit, flag = 0, 0, False
        for charr in s:
            if charr =='0':
                if flag:
                    flag=False
                    res+=limit
            else:
                flag=True
                limit+=1

        return res
