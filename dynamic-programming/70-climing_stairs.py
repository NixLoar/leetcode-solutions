# https://leetcode.com/problems/climbing-stairs/submissions/1423698864
from functools import cache
@cache
def climbStairs(self, n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return self.climbStairs(n-1) + self.climbStairs(n-2)
