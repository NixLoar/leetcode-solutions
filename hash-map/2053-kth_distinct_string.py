# https://leetcode.com/problems/kth-distinct-string-in-an-array/submissions/1370613841

def kthDistinct(self, arr: List[str], k: int) -> str:
    hashmap = {}
    for string in arr:
        if string in hashmap:
            hashmap[string] += 1
        else: 
            hashmap[string] = 1
    for key,val in hashmap.items():
        if val == 1:
            k -= 1
            if k == 0:
                return key
    return ''