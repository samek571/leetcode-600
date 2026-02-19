class Solution:
    def deVowel(self, s):
        return ''.join('*' if c in 'aeiou' else c for c in s)

    def spellchecker(self, wordlist, queries):
        exact = set(wordlist)
        caseMap = {}
        vowelMap = {}

        for w in wordlist:
            lower = w.lower()
            devowel = self.deVowel(lower)
            if lower not in caseMap:
                caseMap[lower] = w
            if devowel not in vowelMap:
                vowelMap[devowel] = w

        res = []
        for q in queries:
            if q in exact:
                res.append(q)
            else:
                lower = q.lower()
                devowel = self.deVowel(lower)
                if lower in caseMap:
                    res.append(caseMap[lower])
                elif devowel in vowelMap:
                    res.append(vowelMap[devowel])
                else:
                    res.append("")
        return res


