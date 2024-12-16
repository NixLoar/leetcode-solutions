# https://leetcode.com/problems/rle-iterator/submissions/1443184466

class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.curr = 0

    def next(self, n: int) -> int:
        while self.curr < len(self.encoding):
            count = self.encoding[self.curr]
            value = self.encoding[self.curr + 1]
            if n <= count:
                self.encoding[self.curr] -= n
                return value
            else:
                n -= count
                self.curr += 2 
        return -1