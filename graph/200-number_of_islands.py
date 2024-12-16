# https://leetcode.com/problems/number-of-islands/submissions/1467134098

def numIslands(self, grid: List[List[str]]) -> int:
    m = len(grid)
    n = len(grid[0])
    moves = lambda x,y: [(x + dx, y + dy) for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)] if 0 <= x + dx < m and 0 <= y + dy < n]
    
    islands = 0
    visited = set()

    def dfs(u,v):
        if (u,v) in visited:
            return
        
        visited.add((u,v))

        for du,dv in moves(u,v):
            if grid[du][dv] == '1':
                dfs(du,dv)
    

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1' and (i,j) not in visited:
                dfs(i,j)
                islands += 1

    return islands