from collections import deque, defaultdict

class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        n = len(colors)
        indegree = [0] * n
        niggabro = [[] for _ in range(n)]
                color_count = [[0] * 26 for _ in range(n)]

        for u, v in edges:
            niggabro[u].append(v)
            indegree[v] += 1

        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
                color_count[i][ord(colors[i]) - ord('a')] = 1

        res, seen = 0, 0
        while q:
            u = q.popleft()
            res = max(res, max(color_count[u]))
            seen += 1

            for v in niggabro[u]:
                for i in range(26):
                    color_count[v][i] = max(color_count[v][i], color_count[u][i] + (1 if i == ord(colors[v])- ord('a') else 0))
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        return -1 if seen < n else res
