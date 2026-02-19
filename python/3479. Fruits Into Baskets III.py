class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        sqrt_ = isqrt(n)
        seen = [0] * (sqrt_ + 2)

        for i in range(n):
            seen[i // sqrt_] = max(seen[i // sqrt_], baskets[i])

        res = 0
        for fruit in fruits:
            seq = -1
            for i in range(sqrt_ + 2):
                if seen[i] >= fruit:
                    seq = i
                    break

            if seq == -1:
                res += 1
                continue

            for i in range(seq * sqrt_, min(n, (seq + 1) * sqrt_)):
                if baskets[i] >= fruit:
                    baskets[i] = 0
                    break

            seen[seq] = 0
            for i in range(seq * sqrt_, min(n, (seq + 1) * sqrt_)):
                seen[seq] = max(seen[seq], baskets[i])

        return res
