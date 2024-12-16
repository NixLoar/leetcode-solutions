# https://leetcode.com/problems/find-center-of-star-graph/submissions/1466827831

def findCenter(self, edges: List[List[int]]) -> int:
    n = len(edges) + 1
    count_neighbors = [0 for i in range(n+1)]
    
    for u,v in edges:
        count_neighbors[u] += 1
        count_neighbors[v] += 1
    
    for i in range(1, n+1):
        if count_neighbors[i] == n-1:
            return i