# https://leetcode.com/problems/height-checker/submissions/1378270818

def heightChecker(self, heights: List[int]) -> int:
    minVal, maxVal = heights[0], heights[0]
    for i in range(len(heights)):
        if maxVal < heights[i]: 
            maxVal = heights[i]
        elif minVal > heights[i]:
            minVal = heights[i]

    counting = {num: 0 for num in heights}
    for num in heights:
        counting[num] += 1 
        
    j = 0
    result = 0
    for i in range(minVal, maxVal+1):
        while counting.get(i,0) > 0:
            if heights[j] != i:
                result += 1
            heights[j] = i
            j += 1
            counting[i] -= 1
    
    return result