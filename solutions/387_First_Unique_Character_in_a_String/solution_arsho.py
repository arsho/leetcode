"""
Title     : 387. First Unique Character in a String
Category  : Hash Table
URL       : https://leetcode.com/problems/first-unique-character-in-a-string/
Author    : arsho
Created   : 06 September 2020
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        characters = {}
        for i, c in enumerate(s):
            if c in characters:
                characters[c].append(i)
            else:
                characters[c] = [i]
        for c in characters.keys():
            if len(characters[c]) == 1:
                return characters[c][0]
        return -1
