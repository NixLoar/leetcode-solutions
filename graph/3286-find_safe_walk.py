# https://leetcode.com/problems/find-a-safe-walk-through-a-grid/submissions/1471436428

def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
    m = len(grid)
    n = len(grid[0])
    
    get_moves = lambda x,y: [(dx,dy) for dx,dy in [(x-1,y), (x+1, y), (x, y-1), (x, y+1)] if 0 <= dx < m and 0 <= dy < n]

    health_to = [[float('inf') for _ in range(n)] for _ in range(m)]
    health_to[0][0] = grid[0][0]

    min_heap = [(grid[0][0],0,0)]

    while min_heap:
        dmg, r, c = heappop(min_heap)

        if r == m-1 and c == n-1:
            return health - dmg > 0
        
        for nr,nc in get_moves(r,c):
            new_dmg = dmg + grid[nr][nc]
            if health_to[nr][nc] > new_dmg:
                health_to[nr][nc] = new_dmg
                heappush(min_heap,(new_dmg,nr,nc))