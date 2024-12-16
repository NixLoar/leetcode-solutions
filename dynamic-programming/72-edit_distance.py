# https://leetcode.com/problems/edit-distance/submissions/1444330425

from functools import cache
def minDistance(self, word1: str, word2: str) -> int:
    @cache
    def recursive(curr1, curr2):
        if curr1 >= len(word1):
            return len(word2) - curr2

        if curr2 >= len(word2):
            return len(word1) - curr1
        
        if word1[curr1] == word2[curr2]:
            return recursive(curr1+1, curr2+1)

        return 1 + min(recursive(curr1+1,curr2), recursive(curr1+1, curr2+1), recursive(curr1,curr2+1))

    return recursive(0, 0)