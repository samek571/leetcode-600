class Solution:
    def maxDifference(self, digits: str, min_length: int) -> int:
        n = len(digits)
        max_diff = float('-inf')

        for a in range(5):
            for b in range(5):
                if a == b:
                    continue

                count_a: List[int] = [0] + list(accumulate((int(ch) == a) for ch in digits))
                count_b: List[int] = [0] + list(accumulate((int(ch) == b) for ch in digits))

                best_by_parity = [[float('-inf')] * 2 for _ in range(2)]
                left = 0

                for right in range(min_length, n + 1):
                    while right - left >= min_length and count_a[right] > count_a[left] and count_b[right] > count_b[left]:
                        pa = count_a[left] % 2
                        pb = count_b[left] % 2
                        best_by_parity[pa][pb] = max(best_by_parity[pa][pb], count_b[left] - count_a[left])
                        left += 1

                    pa = count_a[right] % 2
                    pb = count_b[right] % 2
                    candidate = best_by_parity[1 - pa][pb]
                    if candidate != float('-inf'):
                        max_diff = max(max_diff, (count_a[right] - count_b[right]) + candidate)

        return -1 if max_diff == float('-inf') else max_diff
