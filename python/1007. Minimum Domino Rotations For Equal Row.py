class Solution:
    def minDominoRotations(self, tops, bottoms):
        board, n = {tops[0], bottoms[0]}, len(tops)

        lower_hsh, upper_hsh = defaultdict(int), defaultdict(int)
        upper_hsh[tops[0]] += 1
        lower_hsh[bottoms[0]] += 1

        for idx in range(1, n):
            upper_hsh[tops[idx]] += 1
            lower_hsh[bottoms[idx]] += 1

            tmp_board = {tops[idx], bottoms[idx]}
            board &= tmp_board
            if not board:
                return -1


        res = float('inf')
        for x in board:
            res = min(res, n - upper_hsh[x], n - lower_hsh[x])

        return res if res != float('inf') else -1
