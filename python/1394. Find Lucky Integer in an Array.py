class Solution:
    def findLucky(self, arr: List[int]) -> int:
        x = collections.Counter(arr)
        cnt = -1
        for key,val in x.items():
            if key == val: cnt = max(cnt, key)

        return cnt
