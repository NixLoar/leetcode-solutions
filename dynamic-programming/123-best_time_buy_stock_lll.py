# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/submissions/1446276830

from functools import cache
def maxProfit(self, prices: List[int]) -> int:
    @cache
    def rec(curr_day, count):
        if curr_day > len(prices)-1:
            return 0

        if count == 4:
            return 0

        if count % 2 == 0:
            return max(rec(curr_day+1, count+1) - prices[curr_day], rec(curr_day+1, count))

        else:
            return max(rec(curr_day+1, count+1) + prices[curr_day], rec(curr_day+1, count))

    return rec(0, 0)