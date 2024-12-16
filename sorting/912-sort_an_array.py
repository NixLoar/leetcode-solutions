# https://leetcode.com/problems/sort-an-array/submissions/1378247761

def sortArray(self, nums: List[int]) -> List[int]:
    minVal, maxVal = nums[0], nums[0]
    for i in range(len(nums)):
        if maxVal < nums[i]: 
            maxVal = nums[i]
        elif minVal > nums[i]:
            minVal = nums[i]

    counting = {num: 0 for num in nums}
    for num in nums:
        counting[num] += 1 
        
    j = 0
    for i in range(minVal, maxVal+1):
        while counting.get(i,0) > 0:
            nums[j] = i
            j += 1
            counting[i] -= 1
    
    return nums