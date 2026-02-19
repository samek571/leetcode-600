class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)

        skill = list(accumulate(skill))
        skill0 = skill[0]
        start = 0

        for j in range(1, m):
            curr = mana[j]
            prev = mana[j - 1]
            t_max = skill0 * prev
            for i in range(1, n):
                t_max = max(t_max, skill[i] * prev - skill[i - 1] * curr)
            start += t_max

        return start + skill[-1] * mana[-1]
