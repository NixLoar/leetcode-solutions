# https://leetcode.com/problems/repeated-dna-sequences/submissions/1386763154

def findRepeatedDnaSequences(self, s: str) -> List[str]:
    if len(s)<10:
        return []
    
    p1 = 0
    p2 = 9
    str_dic = {}
    for p2 in range(10, len(s)+1):
        print(p1,p2,s[p1:p2])
        if s[p1:p2] in str_dic:
            str_dic[s[p1:p2]] += 1
        else:
            str_dic[s[p1:p2]] = 1
        p1+=1

    result = []
    for aux in str_dic:
        if str_dic[aux] > 1:
            result.append(aux)

    return result