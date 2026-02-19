class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:

        res = _sum = sum(map(mul, prices, strategy))

        for idx in range(len(prices)):
            _sum += prices[idx] * (1 - strategy[idx])
            if idx >= k//2:
                _sum -= prices[idx - k//2]
            if idx >= k:
                _sum += prices[idx - k] * strategy[idx - k]
            if idx >= k-1 and res < _sum:
                res = _sum

        return res
