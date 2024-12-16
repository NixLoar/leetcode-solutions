# https://leetcode.com/problems/fibonacci-number/submissions/1337677180

def fib(self, n: int) -> int:
    if n<=1:
        return n
    a = 0 
    b = 1
    for i in range(2, n+1):
        b, a = a + b, b
    return b