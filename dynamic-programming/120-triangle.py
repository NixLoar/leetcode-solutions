# https://leetcode.com/problems/triangle/submissions/1446235561

def minimumTotal(self, triangle: List[List[int]]) -> int:
    n = len(triangle)
    for i in range(n - 2, -1, -1):
        qtd = i + 1
        for j in range(qtd):
            res = min(triangle[i + 1][j], triangle[i + 1][j + 1]) + triangle[i][j]
            triangle[i][j] = res
    return triangle[0][0]