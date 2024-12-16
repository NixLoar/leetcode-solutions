# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/submissions/1469708684

def minimumObstacles(self, grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    
    get_moves = lambda x,y: [(dx,dy) for dx,dy in [(x-1,y), (x+1, y), (x, y-1), (x, y+1)] if 0 <= dx < m and 0 <= dy < n]

    obstacles = [[float('inf') for _ in range(n)] for _ in range(m)]
    obstacles[0][0] = 0

    min_heap = [(0,0,0)]

    while min_heap:
        o,r,c = heappop(min_heap)

        if r == m-1 and c == n-1:
            return o

        for nr, nc in get_moves(r,c):
            if o+grid[nr][nc] < obstacles[nr][nc]:
                obstacles[nr][nc] = o+grid[nr][nc]
                heappush(min_heap, (o+grid[nr][nc],nr,nc))