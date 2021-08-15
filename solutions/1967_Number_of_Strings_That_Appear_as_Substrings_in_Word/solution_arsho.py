"""
Title     : 1967. Number of Strings That Appear as Substrings in Word
Category  : String
URL       : https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/
Author    : arsho
Created   : 15 August 2021
"""
from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum([1 for c in patterns if c in word])
