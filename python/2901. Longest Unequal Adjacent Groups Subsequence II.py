class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        next_idx = [-1] * n
        l = [1] * n
        ans = 1
        longest_start_idx = 0

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if len(words[i]) == len(words[j]):

                    diff = 0
                    for k in range(len(words[i])):
                        if words[i][k] != words[j][k]:
                            diff += 1
                            if diff > 1:
                                break

                    if diff == 1 and groups[i] != groups[j]:
                        if next_idx[i] == -1 or l[j] > l[next_idx[i]]:
                            next_idx[i] = j
                            l[i] = l[j] + 1
                            if l[i] > ans:
                                ans = l[i]
                                longest_start_idx = i

        res = []
        while longest_start_idx != -1:
            res.append(words[longest_start_idx])
            longest_start_idx = next_idx[longest_start_idx]

        return res
