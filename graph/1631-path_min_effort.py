# https://leetcode.com/problems/path-with-minimum-effort/submissions/1467847550

def minimumEffortPath(self, heights: List[List[int]]) -> int:
    m = len(heights)
    n = len(heights[0])
    
    get_moves = lambda x,y: [(dx,dy) for dx,dy in [(x-1,y), (x+1, y), (x, y-1), (x, y+1)] if 0 <= dx < m and 0 <= dy < n]

    effort = [[float('inf') for _ in range(n)] for _ in range(m)]

    effort[0][0] = 0
    min_heap = [(0,0,0)]

    while min_heap:
        e,r,c = heappop(min_heap)

        if r == m - 1 and c == n - 1:
            return e
        
        for nr, nc in get_moves(r,c):
            ne = max(e, abs(heights[r][c] - heights[nr][nc]))

            if ne < effort[nr][nc]:
                effort[nr][nc] = ne
                heappush(min_heap, (ne,nr,nc))