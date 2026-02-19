class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:

        res, prev= 0,0
        for floor in bank:
            curr = floor.count('1')
            if curr > 0:
                res += prev * curr
                prev = curr

        return res
