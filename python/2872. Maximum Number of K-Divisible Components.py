class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        self.res, adj = 0, defaultdict(list)

        for u, v in edges:
            adj[v].append(u)
            adj[u].append(v)

        def dfs(node, parent):
            tmp_sum = values[node]
            for neighbor in adj[node]: #branch recurse
                if neighbor != parent:
                    tmp_sum += dfs(neighbor, node)

            if tmp_sum%k == 0: #exit
                self.res += 1
                return 0

            return tmp_sum%k

        dfs(0, -1)
        return self.res
