from typing import List
from collections import defaultdict

class Solution:
    def dfs(self, adj: defaultdict, visited: List[bool], src: int, target: int) -> bool:
        visited[src] = True

        if src == target:
            return True

        is_prerequisite = False
        for adj_node in adj[src]:
            if not visited[adj_node]:
                is_prerequisite = is_prerequisite or self.dfs(adj, visited, adj_node, target)
        
        return is_prerequisite

    def preprocess(self, numCourses: int, adj_list: defaultdict, is_prerequisite: List[List[bool]]) -> None:
        for u in range(numCourses):
            for v in range(numCourses):
                if u != v:
                    visited = [False] * numCourses
                    if self.dfs(adj_list, visited, u, v):
                        is_prerequisite[u][v] = True

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = defaultdict(list)
        for edge in prerequisites:
            adj_list[edge[0]].append(edge[1])

        is_prerequisite = [[False for _ in range(numCourses)] for _ in range(numCourses)]
        self.preprocess(numCourses, adj_list, is_prerequisite)

        result = []
        for u, v in queries:
            result.append(is_prerequisite[u][v])

        return result
