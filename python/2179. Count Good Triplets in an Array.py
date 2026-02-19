from typing import List

#copied this shit
class FenwickTree:
    def __init__(self, size: int):
        self.tree = [0] * (size + 1)
        self.size = size

    def update(self, i: int, delta: int):
        i += 1
        while i <= self.size:
            self.tree[i] += delta
            i += i & -i

    #prefix sums
    def query(self, i: int) -> int:
        i += 1
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        index_map = {num: i for i, num in enumerate(nums2)}
        indices = [index_map[num] for num in nums1]

        left_tree = FenwickTree(n)
        left_counts = []
        for idx in indices:
            count = left_tree.query(idx - 1)
            left_counts.append(count)
            left_tree.update(idx, 1)

        right_tree = FenwickTree(n)
        right_counts = [0] * n
        for i in range(n - 1, -1, -1):
            idx = indices[i]
            count = right_tree.query(n - 1) - right_tree.query(idx)
            right_counts[i] = count
            right_tree.update(idx, 1)

        return sum(l * r for l, r in zip(left_counts, right_counts))
