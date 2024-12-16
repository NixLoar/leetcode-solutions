# https://leetcode.com/problems/decode-string/submissions/1385905474

def decodeString(self, s: str) -> str:
    def generateString(i) -> str:
        result = ''
        while i < len(s):
            if s[i].isdigit():
                num = ''
                while s[i].isdigit():
                    num += s[i]
                    i+=1
                i, aux_str = generateString(i+1)
                result += int(num)*aux_str
            elif s[i] == ']':
                return(i+1, result)
            else: 
                result += s[i]
                i+=1
        return i, result
    
    i, decoded = generateString(0)
    return decoded