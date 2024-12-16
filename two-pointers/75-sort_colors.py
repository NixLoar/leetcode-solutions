# https://leetcode.com/problems/sort-colors/submissions/1337406278

def sortColors(self, nums: List[int]) -> None:
    l, m, h = 0, 0, len(nums)-1
    while m <= h:
        if nums[m] == 0:
            nums[m], nums[l] = nums[l], nums[m]
            l += 1
            m += 1

        elif nums[m] == 1:
            m += 1

        elif nums[m] == 2:
            nums[m], nums[h] = nums[h], nums[m]
            h += -1