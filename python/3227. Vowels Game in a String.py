class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return bool(set(s) & set("aeiou"))
