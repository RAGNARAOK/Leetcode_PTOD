from collections import deque, defaultdict

def is_bipartite(adj, curr, colors, curr_color):
        colors[curr] = curr_color
        
        for ngbr in adj[curr]:
            if colors[ngbr] == colors[curr]:
                return False
            
            if colors[ngbr] == -1:
                if not is_bipartite(adj, ngbr, colors, 1 - curr_color):
                    return False
        
        return True

def bfs(adj, curr_node, n):
        que = deque([curr_node])
        visited = [False] * n
        visited[curr_node] = True
        
        level = 1  # max groups in that component
        while que:
            size = len(que)
            for _ in range(size):
                curr = que.popleft()
                
                for ngbr in adj[curr]:
                    if not visited[ngbr]:
                        que.append(ngbr)
                        visited[ngbr] = True
            
            level += 1  # One extra increment in the last loop
        
        return level - 1

def get_max_from_each_comp(adj, curr, visited, levels):
        max_grp = levels[curr]
        visited[curr] = True
        
        for ngbr in adj[curr]:
            if not visited[ngbr]:
                max_grp = max(max_grp, get_max_from_each_comp(adj, ngbr, visited, levels))
        
        return max_grp
class Solution:
    

    
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
    
        for u, v in edges:
            u, v = u - 1, v - 1  # Converting to 0-based index
            adj[u].append(v)
            adj[v].append(u)
        
        # Bipartite check
        colors = [-1] * n
        for node in range(n):
            if colors[node] == -1:
                if not is_bipartite(adj, node, colors, 1):
                    return -1
        
        # BFS to find max levels for each node
        levels = [0] * n
        for node in range(n):
            levels[node] = bfs(adj, node, n)
        
        max_group_each_comp = 0
        visited = [False] * n
        for node in range(n):
            if not visited[node]:
                max_group_each_comp += get_max_from_each_comp(adj, node, visited, levels)
        
        return max_group_each_comp
