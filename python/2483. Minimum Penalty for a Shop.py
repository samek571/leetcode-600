class Solution:
    def bestClosingTime(self, customers: str) -> int:

        best, tmp, best_hour = 0, 0, -1

        for idx, c in enumerate(customers):
            tmp += -1 if c == 'N' else 1

            if tmp > best:
                best, best_hour = tmp, idx

        return best_hour + 1
