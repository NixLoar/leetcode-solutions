# https://leetcode.com/problems/remove-methods-from-project/submissions/1471404838

def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
    adj = [[] for _ in range (n)]

    for a,b in invocations:
        adj[a].append(b)

    suspects = set()
    queue = deque([k])

    while queue:
        curr = queue.popleft()
        suspects.add(curr)

        for neighbor in adj[curr]:
            if neighbor not in suspects:
                suspects.add(neighbor)
                queue.append(neighbor)
    
    for a,b in invocations:
        if b in suspects and a not in suspects:
            return [i for i in range(n)]

    return [i for i in range(n) if i not in suspects]