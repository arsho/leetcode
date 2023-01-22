"""
Title     : 1704. Determine if String Halves Are Alike
Category  : String
URL       : https://leetcode.com/problems/determine-if-string-halves-are-alike/
Author    : arsho
Created   : 21 January 2023
"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u',
                  'A', 'E', 'I', 'O', 'U']
        total_vowels = 0
        x = len(s)
        start_pointer = 0
        end_pointer = x - 1
        for i in range(x // 2):
            if s[start_pointer] in vowels:
                total_vowels += 1
            if s[end_pointer] in vowels:
                total_vowels -= 1
            start_pointer += 1
            end_pointer -= 1
        return total_vowels == 0
