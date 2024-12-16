# https://leetcode.com/problems/find-if-path-exists-in-graph/submissions/1466853021

def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    if not edges:
        return True

    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []

        if v not in graph:
            graph[v] = []

        graph[u].append(v)
        graph[v].append(u)
    
    visited = set()
    
    def dfs(node): 
        if node in visited:
            return
        
        visited.add(node)
    
        for neighbor in graph[node]:
            dfs(neighbor)

    dfs(source)
    return destination in visited