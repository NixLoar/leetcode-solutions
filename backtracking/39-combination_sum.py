# https://leetcode.com/problems/combination-sum/submissions/1418564885

def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    output = []

    def backtracking(partial, remains, index):
        if remains == 0:
            output.append(partial.copy())
            return
        if remains < 0:
            return 

        for i in range(index, len(candidates)):
            partial.append(candidates[i])
            backtracking(partial, remains-candidates[i], i)
            partial.pop()

    backtracking([], target, 0)
            
    return output