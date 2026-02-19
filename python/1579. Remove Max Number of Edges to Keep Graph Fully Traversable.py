#MST Kruskal

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0] * (n+1)
        self.cp = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootY] > self.rank[rootX]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        self.cp -= 1
        return True

    def connected(self):
        return self.cp == 1


class Solution:
    def maxNumEdgesToRemove(self, n, edges):
        ed = len(edges)
        a = UnionFind(n)
        b = UnionFind(n)
        edgs = 0

        for e in edges:
            if e[0] == 3:
                if a.unite(e[1], e[2]) | b.unite(e[1], e[2]):
                    edgs += 1

        for e in edges:
            if e[0] == 1:
                if a.unite(e[1], e[2]):
                    edgs += 1
            elif e[0] == 2:
                if b.unite(e[1], e[2]):
                    edgs += 1

        if a.connected() and b.connected():
            return ed - edgs
        return -1
