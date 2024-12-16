# https://leetcode.com/problems/word-search/submissions/1443304687

def exist(self, board: List[List[str]], word: str) -> bool:
    m, n = len(board), len(board[0])
    def recursive(index, row, col):
        if index == len(word) - 1 and board[row][col] == word[index]:
            return True

        if board[row][col] != word[index]:
            return False

        temp = board[row][col]
        board[row][col] = "#"

        for move in validadeMoves(row, col):
            if recursive(index + 1, move[0], move[1]):
                return True

        board[row][col] = temp
        return False

    def validadeMoves(row, col):
        moves = [(row + dx, col + dy) for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]]
        return [(r, c) for r, c in moves if 0 <= r < m and 0 <= c < n]

    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0] and recursive(0, i, j):
                return True

    return False