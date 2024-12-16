# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/submissions/1337702725

def countPairs(self, nums: List[int], target: int) -> int:
    res = 0
    l = 0
    r = 1
    nums.sort()
    while l < len(nums)-1:
        if nums[l] + nums[r] < target:
            res += 1
            if r + 1 == len(nums):
                l += 1
                r = l + 1
            else:
                r += 1
        else:
            l += 1
            r = l + 1
    return res