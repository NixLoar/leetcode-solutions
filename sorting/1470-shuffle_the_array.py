# https://leetcode.com/problems/shuffle-the-array/submissions/1332388836

def shuffle(self, nums: List[int], n: int) -> List[int]:
    result = []
    for i in range(n):
        result.append(nums[i])
        result.append(nums[i+n])
    return result