class Solution(object):
    def _builder(self, edges, size):
        graph = [[] for _ in range(size)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph

    def bfs(self, graph):
        n = len(graph)
        color_count = [0, 0]
        node_color = [0] * n
        seen = [False] * n
        queue = deque([(0, 0)])
        seen[0] = True

        while queue:
            node, color = queue.popleft()
            node_color[node] = color
            color_count[color] += 1

            for neighbor in graph[node]:
                if not seen[neighbor]:
                    seen[neighbor] = True
                    queue.append((neighbor, 1 - color))

        return color_count, node_color

    def maxTargetNodes(self, edges1, edges2):
        n = len(edges1) + 1
        m = len(edges2) + 1

        tree1 = self._builder(edges1, n)
        tree2 = self._builder(edges2, m)

        color1, node_color1 = self.bfs(tree1)
        color2, _ = self.bfs(tree2)

        max_color2 = max(color2)

        res = [0] * n
        for i in range(n):
            res[i] = color1[node_color1[i]] + max_color2

        return res
