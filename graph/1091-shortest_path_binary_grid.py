# https://leetcode.com/problems/shortest-path-in-binary-matrix/submissions/1457732925

def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    if grid[0][0] != 0:
        return -1
    
    n = len(grid)

    get_moves = lambda x, y: [
    (dx, dy) for dx, dy in [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)] if 0 <= dx < n and 0 <= dy < n]

    queue = deque([(0,0,1)])
    visited = set((0,0))

    while queue:
        row, col, path = queue.popleft()

        if row == n-1 and col == n-1:
            return path

        for nr, nc in get_moves(row,col):
            if grid[nr][nc] == 0 and (nr, nc) not in visited:
                queue.append((nr, nc, path+1))
                visited.add((nr, nc))
            
    return -1