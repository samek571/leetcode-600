class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        if not word.isalnum():
            return False

        vowels = set("aeiouAEIOU")
        c1 = any(c in vowels for c in word if c.isalpha())
        c2 = any(c.isalpha() and c not in vowels for c in word)

        return c1 and c2
