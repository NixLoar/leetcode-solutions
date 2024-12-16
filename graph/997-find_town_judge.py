# https://leetcode.com/problems/find-the-town-judge/submissions/1466822724

def findJudge(self, n: int, trust: List[List[int]]) -> int:
    trusted = [[0, False] for i in range(n+1)]

    for a,b in trust:
        trusted[b][0] += 1
        trusted[a][1] = True

    for i in range(1, n+1):
        if trusted[i][0] == n-1 and not trusted[i][1]:
            return i

    return -1