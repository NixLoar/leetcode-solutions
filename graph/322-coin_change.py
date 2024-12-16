# https://leetcode.com/problems/coin-change/submissions/1457750466

def coinChange(self, coins: List[int], amount: int) -> int:
    if amount == 0:
        return 0

    queue = deque([(0, amount)])
    visited = set([amount])

    while queue:
        numCoins, currAmount = queue.popleft()

        for coin in coins:
            if currAmount - coin < 0:
                continue

            if currAmount - coin == 0:
                return numCoins + 1

            if currAmount - coin not in visited:
                queue.append((numCoins + 1, currAmount - coin))
                visited.add(currAmount - coin)

    return -1