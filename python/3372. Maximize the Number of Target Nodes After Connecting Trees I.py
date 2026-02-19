class Solution:
    def maxTargetNodes(self, edges1, edges2, k):
        def bfs(start, adj, k):
            if k == 0: return 1

            seen = set([start])
            q = deque([start])
            _res, lvl = 1, 0
            while q and lvl < k:
                for _ in range(len(q)):
                    node = q.popleft()
                    for nigga in adj[node]:
                        if nigga not in seen:
                            seen.add(nigga)
                            q.append(nigga)
                            _res += 1
                lvl += 1
            return _res


        n = max(max(e) for e in edges1) + 1
        niggers1 = [[] for _ in range(n)]
        for u, v in edges1:
            niggers1[u].append(v)
            niggers1[v].append(u)

        m = max(max(e) for e in edges2) + 1
        niggers2 = [[] for _ in range(m)]
        for u, v in edges2:
            niggers2[u].append(v)
            niggers2[v].append(u)


        res = [bfs(i, niggers1, k) for i in range(n)]

        res2 = 0
        if k > 0:
            for i in range(m):
                res2 = max(res2, bfs(i, niggers2, k - 1))

        return [p + res2 for p in res]
