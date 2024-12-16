# https://leetcode.com/problems/rotate-array/submissions/1337649289

def rotate(self, nums: List[int], k: int) -> None:
    n = len(nums)
    k %= n
    if k == 0: 
        return
    def reverse(s, e):
        while s < e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e += -1
    reverse(0, n-1)
    reverse(0, k-1)
    reverse(k, n-1)