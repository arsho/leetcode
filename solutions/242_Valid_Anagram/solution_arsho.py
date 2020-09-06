"""
Title     : 242. Valid Anagram
Category  : Hash Table
URL       : https://leetcode.com/problems/valid-anagram/
Author    : arsho
Created   : 06 September 2020
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        characters = {}
        for c in s:
            characters[c] = characters.get(c, 0) + 1
        for c in t:
            if c not in characters:
                return False
            if characters[c] == 0:
                return False
            characters[c] -= 1
        for c in characters:
            if characters[c] != 0:
                return False
        return True
