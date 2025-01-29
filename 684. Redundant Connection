class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))  
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent == y_parent:
            return

        if self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
        elif self.rank[y_parent] > self.rank[x_parent]:
            self.parent[x_parent] = y_parent
        else:
            self.parent[y_parent] = x_parent  # Make x the parent
            self.rank[x_parent] += 1


class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)
        dsu = DSU(n)

        for u, v in edges:
            if dsu.find(u) == dsu.find(v):
                return [u, v]
            dsu.union(u, v)

        return []
