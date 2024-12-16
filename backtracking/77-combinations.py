# https://leetcode.com/problems/combinations/submissions/1416323919

def combine(self, n: int, k: int) -> List[List[int]]:
    combinations = []
    def getAllCombinations(curr_num, k, curr_comb):
        if k == 0:
            combinations.append(curr_comb[:])
            return 
        for i in range(curr_num, n+1):
            curr_comb.append(i)
            getAllCombinations(i+1, k-1, curr_comb)
            curr_comb.pop()
        return
    getAllCombinations(1, k, [])
    return combinations