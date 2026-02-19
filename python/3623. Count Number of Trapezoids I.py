class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        y_freq, total_pairs, sum_pair_squares = Counter(p[1] for p in points), 0, 0

        for cnt in y_freq.values():
            if cnt <= 1:
                continue

            pairs_at_y = cnt*(cnt-1)//2
            total_pairs += pairs_at_y
            sum_pair_squares += pairs_at_y*pairs_at_y

        return (total_pairs*total_pairs - sum_pair_squares)//2 % (10**9+7)
