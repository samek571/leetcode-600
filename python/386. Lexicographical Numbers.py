class Solution:
    #idea is a tree with branching factor 10
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        count = 1
        for _ in range(n):
            res.append(count)
            if count * 10 <= n:
                count *= 10
            else:
                if count >= n:
                    count //= 10
                count += 1
                while count % 10 == 0:
                    count //= 10
        return res
