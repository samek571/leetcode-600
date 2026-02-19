class Solution:
    def countTrapezoids(self, points):
        parallel_groups = {}
        collinear_groups = {}
        n = len(points)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy

                g = self.gcd(dx, abs(dy))
                norm_dx = dx // g
                norm_dy = dy // g

                line_constant = norm_dx * y1 - norm_dy * x1

                slope_key = (norm_dx << 12) | (norm_dy + 2000)
                direction_key = (dx << 12) | (dy + 2000)

                parallel_groups.setdefault(slope_key, {}).setdefault(line_constant, 0)
                parallel_groups[slope_key][line_constant] += 1

                collinear_groups.setdefault(direction_key, {}).setdefault(line_constant, 0)
                collinear_groups[direction_key][line_constant] += 1

        return self.count_pairs(parallel_groups) - self.count_pairs(collinear_groups) // 2


    def count_pairs(self, groups):
        res = 0
        for line_map in groups.values():
            segment_sum = sum(line_map.values())
            remaining = segment_sum
            for count in line_map.values():
                remaining -= count
                res += count * remaining
        return res


    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return abs(a)
