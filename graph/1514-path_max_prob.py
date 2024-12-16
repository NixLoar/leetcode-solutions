# https://leetcode.com/problems/path-with-maximum-probability/submissions/1459600910

def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
    neighbors = [[] for _ in range(n+1)]

    for i in range(len(edges)):
        neighbors[edges[i][0]].append((edges[i][1],succProb[i]))
        neighbors[edges[i][1]].append((edges[i][0],succProb[i]))
    
    min_prob = [0] * (n)
    min_prob[start_node] = 1

    queue = deque([(start_node, 0)])

    while queue:
        curr, prob = queue.popleft()

        for neighbor, edge_prob in neighbors[curr]:
            if prob > 0:
                new_prob = prob * edge_prob
            else:
                new_prob = edge_prob

            if new_prob > min_prob[neighbor]:
                min_prob[neighbor] = new_prob
                queue.append((neighbor, new_prob))
    
    return min_prob[end_node]