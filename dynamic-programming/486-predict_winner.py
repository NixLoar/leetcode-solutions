# https://leetcode.com/problems/predict-the-winner/submissions/1446253705

from functools import cache
def predictTheWinner(self, nums: List[int]) -> bool:
    @cache
    def rec(p1, p2):
        if p1 > p2:
            return 0

        return max(nums[p1] - rec(p1+1, p2), nums[p2] - rec(p1, p2-1))

    return rec(0, len(nums)-1) >= 0