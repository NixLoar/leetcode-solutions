# https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/submissions/1443416544

def twoEggDrop(self, n: int) -> int:
    for i in range(1,n+1):
        if n - i <= 0:
            break
        n -= i
    return i