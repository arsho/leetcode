"""
Title     : 2481. Minimum Cuts to Divide a Circle
Category  : Math
URL       : https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/
Author    : arsho
Created   : 21 January 2023
"""


class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2 == 0:
            return n // 2
        return n
