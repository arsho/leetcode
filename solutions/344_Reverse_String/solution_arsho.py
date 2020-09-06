"""
Title     : 344. Reverse String
Category  : Two Pointers
URL       : https://leetcode.com/problems/reverse-string/
Author    : arsho
Created   : 06 September 2020
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]


# Alternative Solution
"""
class Solution(object):
    def reverseString(self, s):
        return s[::-1]
"""
