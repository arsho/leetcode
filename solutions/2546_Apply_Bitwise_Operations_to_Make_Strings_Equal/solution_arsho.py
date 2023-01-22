"""
Title     : 2546. Apply Bitwise Operations to Make Strings Equal
Category  : String
URL       : https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/
Author    : arsho
Created   : 22 January 2023
"""


class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        s_0 = s.count("0")
        s_1 = s.count("1")
        t_0 = target.count("0")
        t_1 = target.count("1")
        if s == target:
            return True
        if s_0 != 0 and s_1 != 0 and t_0 != 0 and t_1 != 0:
            return True
        if s_0 != 0 and s_1 == 0 and t_1 != 0:
            return False
        if s_1 != 0 and t_1 != 0:
            return True
        return s_0 == t_0 and s_1 == t_1
