class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        knows = [1] + [0] * 999

        shared, res = 0, 1
        for day in range(delay, forget):
            shared += knows[day - delay]
            res += shared
            knows[day] = shared

        for day in range(forget, n):
            shared += knows[day - delay] - knows[day - forget]
            res += shared - knows[day - forget]
            knows[day] = shared

        return res % (10**9+7)
