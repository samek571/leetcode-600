class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = Counter(word)
        res = len(word)

        for minF in freq.values():
            tmp_res = 0
            for subj in freq.values():

                if subj > minF + k: tmp_res += subj - minF - k
                elif subj < minF: tmp_res += subj

            res = min(res, tmp_res)

        return res
