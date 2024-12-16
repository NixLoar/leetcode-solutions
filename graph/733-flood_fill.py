# https://leetcode.com/problems/flood-fill/submissions/1457755174

def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    m, n = len(image), len(image[0])

    if image[sr][sc] == color:
        return image
    
    old_color = image[sr][sc]

    get_moves = lambda x, y: [(dx, dy) for dx, dy in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] if 0 <= dx < m and 0 <= dy < n ]

    queue = deque([(sr,sc)])
    visited = set((sr,sc))

    while queue:
        r, c = queue.popleft()

        if image[r][c] == old_color:
            image[r][c] = color
        
        for nr, nc in get_moves(r,c):
            if image[nr][nc] == old_color and (nr,nc) not in visited:
                queue.append((nr,nc))
                visited.add((nr,nc))
    
    return image