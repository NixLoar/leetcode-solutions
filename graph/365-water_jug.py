# https://leetcode.com/problems/water-and-jug-problem/submissions/1469665973

def canMeasureWater(self, x: int, y: int, target: int) -> bool:
    if x + y < target:
        return False
    
    if x + y == target:
        return True
    
    queue = deque([(x,0),(0,y)])
    visited = set()

    while queue:
        j1, j2 = queue.popleft()

        if j1 + j2 == target:
            return True
        
        if j1 < x and (x,j2) not in visited:
            queue.append((x,j2))
            visited.add((x,j2))

        if j2 < y and (j1,y) not in visited:
            queue.append((j1,y))
            visited.add((j1,y))
    
        if (0,j2) not in visited:
            queue.append((0,j2))
            visited.add((0,j2))
        
        cap_j2 = y - j2
        if j1 >= cap_j2 and (j1-cap_j2, y) not in visited:
            queue.append((j1-cap_j2, y))
            visited.add((j1-cap_j2, y))

        if j1 < cap_j2 and (0, j2 + j1) not in visited:
            queue.append((0, j2 + j1))
            visited.add((0, j2 + j1))

        if (j1,0) not in visited:
            queue.append((j1,0))
            visited.add((j1,0))

        cap_j1 = x - j1
        if j2 >= cap_j1 and (x, j2-cap_j1) not in visited:
            queue.append((x, j2-cap_j1))
            visited.add((x, j2-cap_j1))

        if j2 < cap_j1 and (j2 + j1, 0) not in visited:
            queue.append((j2 + j1, 0))
            visited.add((j2 + j1, 0))
    
    return False