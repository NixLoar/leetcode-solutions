# https://leetcode.com/problems/network-delay-time/submissions/1459605342

def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    neighbors = [[] for _ in range(n)]

    for u, v, w in times:
        neighbors[u-1].append([v-1, w])

    min_time = [float("inf")] * (n)
    min_time[k-1] = 0

    queue = deque([(k-1,0)])

    while queue:
        curr, time = queue.popleft()

        for neighbor, path_time in neighbors[curr]:
            new_time = time + path_time
            if new_time < min_time[neighbor]:
                min_time[neighbor] = new_time
                queue.append((neighbor, new_time))

    max_time = 0
    for time in min_time:
        if time == float("inf"):
            return -1
        elif time > max_time:
            max_time = time
    
    return max_time