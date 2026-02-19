class Solution:
    #simple bfs does it

    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:

        def _helpr( sub: str, s: str, k: int) -> bool:
            idx, cnt = 0, 0
            for ch in s:
                if ch == sub[idx]:
                    idx += 1
                    if idx == len(sub):
                        cnt += 1
                        idx = 0
                        if cnt == k:
                            return True

            return False


        res, q = "", deque([""])
        while q:
            now = q.popleft()
            for ch in map(chr, range(ord('a'), ord('z') + 1)):
                _next = now + ch
                if _helpr(_next, s, k):
                    res = _next
                    q.append(_next)
        return res
