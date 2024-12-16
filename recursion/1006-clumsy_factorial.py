# https://leetcode.com/problems/clumsy-factorial/submissions/1380512424

def clumsy(self, n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2

    A = n
    B = n - 1
    C = n - 2
    D = n - 3
    E = n - 4  

    return ((A * B) // C + D) + self.clumsyFactorial(E)

def clumsyFactorial(self, n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return -1
    if n == 2:
        return -2

    A = n
    B = n - 1
    C = n - 2
    D = n - 3
    E = n - 4  
    
    return (-((A * B) // C) + D) + clumsyFactorial(E)