# https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/submissions/1428534095

def maxMoves(self, grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    moves = [-1, 0, 1]
    prev_moves = {}
    max_lenght = 0

    def findMaxPath(curr_pos, path_lenght):
        nonlocal max_lenght
        if max_lenght == n-1:
            return

        if path_lenght == n-1:
            max_lenght = n-1
            return

        hasMove = False
        for move in moves:
            if validateMove(move, curr_pos):
                hasMove = True
                next_pos = (curr_pos[0] + move, curr_pos[1] + 1) 
                if next_pos not in prev_moves:
                    prev_moves[next_pos] = findMaxPath(next_pos, path_lenght + 1)
        
        if not hasMove:
            max_lenght = max(max_lenght, path_lenght)
            return path_lenght

    def validateMove(move, curr_pos):
        i,j = curr_pos[0], curr_pos[1]
        
        if i + move < 0 or i + move > m-1:
            return False

        if grid[i+move][j+1] <= grid[i][j]:
            return False

        return True


    for i in range(m):
        if max_lenght < n-1:
            findMaxPath([i,0], 0)
    
    return max_lenght