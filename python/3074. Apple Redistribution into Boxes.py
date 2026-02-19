class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort()

        total, res = sum(apple), 0
        for c in reversed(capacity):
            total -= c
            res += 1
            if total <= 0:
                return res

        return res
