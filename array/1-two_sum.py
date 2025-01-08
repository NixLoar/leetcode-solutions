# https://leetcode.com/problems/two-sum/description/

def twoSum(nums, target):
    p1 = 0
    p2 = 1

    while p1 < len(nums)-1 :
        if nums[p1] + nums[p2] == target:
            return [p1,p2]
        
        if p2 == len(nums)-1:
            p1 += 1
            p2 = p1+1
            continue

        p2 += 1
        
nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))

nums = [3,2,4]
target = 6
print(twoSum(nums, target))