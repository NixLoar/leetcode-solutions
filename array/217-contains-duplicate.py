# https://leetcode.com/problems/contains-duplicate/

def containsDuplicate(nums):
    hashset = set()

    for num in nums:
        if num in hashset:
            return True
        
        hashset.add(num)

    return False

nums1 = [1,2,3,4,1]
nums2 = [1,2,3,4]
print(containsDuplicate(nums1))
print(containsDuplicate(nums2))