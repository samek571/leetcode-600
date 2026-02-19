class Solution:
    from typing import List
    import itertools

    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        # if len(s) % k != 0:
        #     s += fill * (k - len(s) % k)

        # return list(itertools.batched(s, k))

        #return [''.join(chunk) for chunk in itertools.batched(s, k)]

        rem = len(s) % k
        if rem: s += fill * (k - rem)

        return [s[i:i + k] for i in range(0, len(s), k)]
