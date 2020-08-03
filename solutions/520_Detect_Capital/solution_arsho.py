"""
Title     : 520. Detect Capital
Category  : String
URL       : https://leetcode.com/problems/detect-capital/
Author    : arsho
Created   : 03 August 2020
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        lower_case = word.lower()
        upper_case = word.upper()
        title_case = word.title()
        return word in [lower_case, upper_case, title_case]
