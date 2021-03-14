"""
Title     : 1790. Check if One String Swap Can Make Strings Equal
Category  : String
URL       : https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/
Author    : arsho
Created   : 15 March 2021
"""


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        mismatched_positions = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                mismatched_positions.append(i)
                if len(mismatched_positions) > 2:
                    return False
        total_mismatched = len(mismatched_positions)
        if total_mismatched == 0:
            return True
        if total_mismatched == 2:
            return s1[mismatched_positions[0]] == s2[
                mismatched_positions[1]] and s1[mismatched_positions[1]] == s2[
                       mismatched_positions[0]]
        return False
