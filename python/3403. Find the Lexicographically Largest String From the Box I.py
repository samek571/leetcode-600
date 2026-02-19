class Solution:
    def answerString(self, word: str, numFriends: int) -> str:

        if numFriends == 1:
            return word

        n = len(word)
        maxLen = n - numFriends + 1

        ans = ""
        for i in range(n):
            ans = max(ans, word[i:i + maxLen])

        return ans
