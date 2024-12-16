# https://leetcode.com/problems/roman-to-integer/submissions/1385939156

def romanToInt(self, s: str) -> int:
    roman_to_dec = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    result = 0
    for i in range(len(s)):
        if i < len(s) - 1 and roman_to_dec[s[i]] < roman_to_dec[s[i+1]]: 
            result -= roman_to_dec[s[i]]
        else:
            result += roman_to_dec[s[i]]
    return result