class Solution:
    def countInterestingSubarrays(self, nums: List[int], m: int, k: int) -> int:
        n = len(nums)
        dp = [0] * n
        res = 0
        interesting_cnt = 0
        last_interesting_idx = -1
        delta = m if k == 0 else k

        for curr_idx, num in enumerate(nums):
            if num % m != k: continue

            gap_idx = curr_idx - last_interesting_idx
            last_interesting_idx = curr_idx


            if k == 0:
                res += (gap_idx * (gap_idx - 1)) // 2


            #dp comes in handy
            if interesting_cnt >= delta:
                res += dp[interesting_cnt - delta] * gap_idx

            if interesting_cnt >= m:
                gap_idx += dp[interesting_cnt - m]

            dp[interesting_cnt] = gap_idx
            interesting_cnt += 1


        #ending so its not fucked
        gap_idx = n - last_interesting_idx
        if k == 0:
            res += (gap_idx * (gap_idx - 1)) // 2
        if interesting_cnt >= delta:
            res += dp[interesting_cnt - delta] * gap_idx

        return res
