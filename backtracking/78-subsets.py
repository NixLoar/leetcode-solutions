# https://leetcode.com/problems/subsets/submissions/1415926386

def subsets(self, nums: List[int]) -> List[List[int]]:
    if nums == []:
        return [[]]
    
    partial_subsets = self.subsets(nums[:-1])
    
    complete_subsets = []
    for subset in partial_subsets:
        complete_subsets.append(subset + [nums[-1]])
    
    return partial_subsets + complete_subsets