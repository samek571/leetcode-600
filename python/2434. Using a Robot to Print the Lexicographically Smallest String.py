class Solution:
    def robotWithString(self, s: str) -> str:
        res, _helpr = [], []
        freq = Counter(s)
        _min_char = 'a'

        for c in s:
            if c == _min_char:
                res.append(c)
            else:
                _helpr.append(c)

            freq[c] -= 1
            if freq[c] == 0:
                del freq[c]

            while _min_char <= 'z' and _min_char not in freq:
                _min_char = chr(ord(_min_char) + 1)

            while _helpr and _helpr[-1] <= _min_char:
                res.append(_helpr.pop())

        while _helpr:
            res.append(_helpr.pop())

        return ''.join(res)
