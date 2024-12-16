# https://leetcode.com/problems/longest-increasing-subsequence/submissions/1442200822

def lengthOfLIS(self, nums: List[int]) -> int:
    n = len(nums)
    count_lenght = [1]*n
    max_lenght = 1
    for i in range(1,n):
        for j in range(i):
            if nums[i] > nums[j]:
                count_lenght[i] = max(count_lenght[i], count_lenght[j]+1)
        max_lenght = max(max_lenght, count_lenght[i])
    return max_lenght