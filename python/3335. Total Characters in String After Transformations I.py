class Solution:
    #Deterministic Stack Automat idea
    #encode, fast forward, decode

    def lengthAfterTransformations(self, s: str, t: int) -> int:
        q = deque([0] * 26)
        for i in s:
            q[ord(i)-97] += 1 #ascii trick

        for i in range(t):
            q[0]+= q[25]
            q.appendleft(q.pop())

        return sum(q) % (10**9+7)
