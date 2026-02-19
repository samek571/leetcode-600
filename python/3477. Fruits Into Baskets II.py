class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        seen = [False] * n

        res = 0 #//simple fucking greedy
        for fruit in fruits:

            bool_processed = False
            for idx in range(n):
                if not seen[idx] and baskets[idx] >= fruit:
                    seen[idx] = True
                    bool_processed = True
                    break

            if not bool_processed:
                res += 1

        return res
