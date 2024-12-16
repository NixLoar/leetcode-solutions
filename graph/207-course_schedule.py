# https://leetcode.com/problems/course-schedule/submissions/1463765667

def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    adj = {i: [] for i in range(numCourses)}
    degree = {i: 0 for i in range(numCourses)}
    
    for dest, src in prerequisites:
        adj[src].append(dest)
        degree[dest] += 1
    
    topo_order = []
    queue = deque([node for node in degree if degree[node] == 0])

    while queue:
        curr = queue.popleft()
        topo_order.append(curr)

        for neighbor in adj[curr]:
            degree[neighbor] -= 1
            if degree[neighbor] == 0:
                queue.append(neighbor)
    
    return len(topo_order) == numCourses