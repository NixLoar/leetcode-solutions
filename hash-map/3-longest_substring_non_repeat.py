# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1402136617

def lengthOfLongestSubstring(self, s: str) -> int:
    char_index_map = {}
    start = 0
    max_len = 0

    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = i
        max_len = max(max_len, i - start + 1)

    return max_len