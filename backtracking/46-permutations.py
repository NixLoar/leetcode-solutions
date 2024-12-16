# https://leetcode.com/problems/permutations/submissions/1416175738

def permute(self, nums: List[int]) -> List[List[int]]:
    permutations = []
    def getPermutations(nums, curr_permut):
        if not nums:
            permutations.append(curr_permut[:])
            return 
        for i in range(len(nums)):
            curr_permut.append(nums[i])
            getPermutations(nums[:i]+nums[i+1:], curr_permut)
            curr_permut.pop()
        return 
    getPermutations(nums, [])
    return permutations