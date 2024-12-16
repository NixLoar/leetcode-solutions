# https://leetcode.com/problems/maximum-subarray/submissions/1425857168

def maxSubArray(self, nums: List[int]) -> int:
    max_sum = 0
    for num in nums:
        max_sum = min(num, max_sum)
    curr_sum = max_sum
    for num in nums:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(curr_sum, max_sum)
    return max_sum