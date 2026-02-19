class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        res_sum = 0
        for idx in range(1, len(colors)):
            if colors[idx] == colors[idx - 1]:
                res_sum += min(neededTime[idx], neededTime[idx - 1])
                neededTime[idx] = max(neededTime[idx], neededTime[idx - 1])

        return res_sum
