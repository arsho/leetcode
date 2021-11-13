"""
Title     : 202. Happy Number
Category  : Hash Table
URL       : https://leetcode.com/problems/happy-number/
Author    : arsho
Created   : 22 November 2019
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        while True:
            s = str(n)
            total = sum([int(c) ** 2 for c in s])
            if total == 1:
                return True
            if total in d:
                return False
            d[total] = 1
            n = total
