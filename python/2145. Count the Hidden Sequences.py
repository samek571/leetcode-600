class Solution:
    def numberOfArrays(self, differences: List[int], l: int, u: int) -> int: #lower upper
        #r as rolling
        r_low = r_max = prev = l #i know denotion like this is dangerous in other languages


        for d in differences:
            prev = d + prev
            r_low = min(r_low, prev)
            r_max = max(r_max, prev)
        r_max += (l - r_low)

        if r_max > u: return 0
        return u - r_max + 1
