class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        [res.append(w) for w in words if not res or Counter(w) != Counter(res[-1])]
        return res
