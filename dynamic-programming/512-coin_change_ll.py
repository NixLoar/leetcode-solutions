# https://leetcode.com/problems/coin-change-ii/submissions/1442194575

from functools import cache
def change(self, amount: int, coins: List[int]) -> int:
    @cache
    def recursive(curr_amount, curr_coin):
        if curr_coin == len(coins):
            return 0
        if curr_amount < 0:
            return 0
        if curr_amount == 0:
            return 1
        return recursive(curr_amount - coins[curr_coin], curr_coin) + recursive(curr_amount, curr_coin+1)
    return recursive(amount,0)