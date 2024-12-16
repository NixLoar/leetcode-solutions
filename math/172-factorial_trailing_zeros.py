# https://leetcode.com/problems/factorial-trailing-zeroes/submissions/1380526083

def trailingZeroes(self, n: int) -> int:
    i=1
    result = 0
    while n//5**i>=1:
        result += n//5**i
        i+=1
    return result