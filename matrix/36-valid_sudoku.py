# https://leetcode.com/problems/valid-sudoku/submissions/1337445582

def isValidSudoku(self, board: List[List[str]]) -> bool:
    for i in range(0,9):
        for j in range(0,9):
            if board[i][j]!='.' and isRepeated(board, i, j):
                return False
    return True

def isRepeated(self, board, row, col) -> bool:
    for i in range(9):
        if i != row and board[i][col] == board[row][col]:
            return True
        if i!= col and board[row][i] == board[row][col]:
            return True
    subRow = (row//3)*3
    subCol = (col//3)*3
    for i in range(subRow, subRow+3):
        for j in range(subCol, subCol+3):
            if i == row and j == col:
                continue
            if board[i][j] == board[row][col]:
                return True
    return False