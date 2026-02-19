class Solution:
    def clearStars(self, s: str) -> str:
        n,s  = len(s), list(s)
        stck = [[] for _ in range(26)]

        for i in range(n):
            if s[i] == '*':
                for k in range(26):
                    if stck[k]:
                        s[stck[k][-1]] = '#'
                        stck[k].pop()
                        break
            else:
                stck[ord(s[i]) - ord('a')].append(i)

        res = []
        for i in range(n):
            if s[i] != '*' and s[i] != '#':
                res.append(s[i])

        return ''.join(res)
