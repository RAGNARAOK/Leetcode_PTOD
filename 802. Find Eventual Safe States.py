class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}        # Creating hashmap for recoding the safe nodes

        ans = []

        def dfs(i):          #Recursive function
            if i in safe:
                return safe[i]
            safe[i] = False
            for nei in graph[i]:
                if not dfs(nei):
                    return False     
# After this loop ends it means the node is a safe node other wise loop would have ended in between
            safe[i] = True
            return safe[i]


        for i in range(n):
            if dfs(i):
                ans.append(i)

        return ans
