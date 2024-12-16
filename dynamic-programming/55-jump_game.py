# https://leetcode.com/problems/jump-game/submissions/1439396857

def canJump(self, nums: List[int]) -> bool:
    min_jump = 1

    if len(nums) == 1:
        return True

    for i in range(len(nums)-2, -1, -1):
        if nums[i] > 0:
            if min_jump > 1 and nums[i] >= min_jump:
                min_jump = 1
                continue

            if min_jump > 1 and nums[i] < min_jump:
                min_jump += 1
                continue

        if nums[i] == 0:
            min_jump += 1
    
    return min_jump == 1