class Solution:
    def sortVowels(self, s: str) -> str:
        vowels_set = set("AEIOUaeiou")
        vowels = sorted([c for c in s if c in vowels_set])

        j = 0
        res = []
        for c in s:
            if c in vowels_set:
                res.append(vowels[j])
                j += 1
            else:
                res.append(c)

        return ''.join(res)

#idk whats wrong with this
#         j = 0
#         return ''.join(
#             [vowels[j] if c in vowels_set; (j := j+1) else c for c in s]
#         )
