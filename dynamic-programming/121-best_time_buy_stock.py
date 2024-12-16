# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1425924635

def maxProfit(self, prices: List[int]) -> int:
    buy_day = 0
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[buy_day] > prices[i]:
            buy_day = i
        max_profit = max(max_profit, prices[i] - prices[buy_day])
    
    return max_profit