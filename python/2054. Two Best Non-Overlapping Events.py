class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        arr = [(0, False, 0)] * (2*len(events))
        for idx, (start, end, v) in enumerate(events):
            arr[2*idx]=(start, False, v)
            arr[2*idx+1]=(end, True, v)

        arr.sort()
        res, tmp= 0, 0
        for t, bool_end, v in arr:
            if bool_end:
                tmp = max(tmp, v)
            else:
                res = max(res, tmp+v)

        return res
