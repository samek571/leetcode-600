class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:

        n, seen, q, res = len(s), {s}, deque([s]), s

        while q:
            curr = q.popleft()
            if curr < res:
                res = curr

            arr = list(curr)
            for idx in range(1, n, 2):
                arr[idx] = str((int(arr[idx]) + a) % 10)
            to_add = ''.join(arr)

            if to_add not in seen:
                seen.add(to_add)
                q.append(to_add)

            k = b % n
            existing_rotation = curr[-k:] + curr[:-k] if k else curr
            if existing_rotation not in seen:
                seen.add(existing_rotation)
                q.append(existing_rotation)

        return res
