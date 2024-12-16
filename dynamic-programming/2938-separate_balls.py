# https://leetcode.com/problems/separate-black-and-white-balls/submissions/1442829942

def minimumSteps(self, s: str) -> int:   
    last_white = 0
    steps = 0
    for i in range(len(s)):
        if s[i] == '0':
            steps += i - last_white
            last_white += 1
    return steps