class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, l: int, suf: str) -> int:


        def _helper(x: str, suf: str, l: int) -> int:
            if len(x) < len(suf): return 0
            elif len(x) == len(suf): return 1 if x >= suf else 0


            suffix, pref_len, res = x[len(x) - len(suf):] , len(x) - len(suf) , 0
            for i in range(pref_len):
                next_gen = (l + 1) ** (pref_len - i - 1)
                curr = int(x[i])

                if l < curr:
                    res += next_gen * (l + 1)
                    return res

                res += curr * next_gen

            if suffix >= suf:
                res += 1

            return res


        return _helper(str(finish), suf, l) - _helper(str(start - 1), suf, l)
