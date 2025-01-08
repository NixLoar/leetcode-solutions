# https://leetcode.com/problems/valid-anagram/description/

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    letters_of_s = {}

    for l in s:
        if l in letters_of_s:
            letters_of_s[l] += 1
        else:
            letters_of_s[l] = 1
    
    for l in t:
        if l not in letters_of_s:
            return False 
        letters_of_s[l] -= 1

    for l in s:
        if letters_of_s[l] != 0:
            return False

    return True

s1 = "anagram" 
t1 = "nagaram"

s2 = "rat"
t2 = "car"

print(isAnagram(s1,t1))
print(isAnagram(s2,t2))
