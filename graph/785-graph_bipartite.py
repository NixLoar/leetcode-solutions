# https://leetcode.com/problems/is-graph-bipartite/submissions/1466873277

def isBipartite(self, graph: List[List[int]]) -> bool:
    if graph == []:
        return True

    n = len(graph)

    A = set()
    B = set()

    def dfs(node, curr_set):
        if node in curr_set:
            return

        curr_set.add(node)

        if curr_set == A:
            next_set = B

        if curr_set == B:
            next_set = A

        for neighbor in graph[node]:
            dfs(neighbor, next_set)

    for i in range(n):
        if graph[i] == []:
            A.add(i)

        elif i in A or i in B:
            continue

        else:
            dfs(i, A)

    for node in A:
        if node in B:
            return False

    return (len(A) + len(B)) == n