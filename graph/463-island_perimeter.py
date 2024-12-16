# https://leetcode.com/problems/island-perimeter/submissions/1467148067

def islandPerimeter(self, grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    moves = lambda x,y: [(x + dx, y + dy) for dx,dy in [(0,1), (1,0), (0,-1), (-1,0)]]

    perimeter = 0

    def dfs(u,v):
        nonlocal perimeter
        if grid[u][v] == -1:
            return
        
        grid[u][v] = -1

        for r,c in moves(u,v):
            if (r >= m or r < 0) or (c >= n or c < 0):
                perimeter += 1

            elif grid[r][c] == 0:
                perimeter += 1

            else:
                dfs(r,c)
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dfs(i,j)
                break
    
    return perimeter