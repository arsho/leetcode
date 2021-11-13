"""
Title     : 1523. Count Odd Numbers in an Interval Range
Category  : Math
URL       : https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
Author    : arsho
Created   : 27 July 2020
"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odd = 0
        gap = high - low
        if low % 2 == 1:
            odd += 1
            gap -= 1
        if high % 2 == 1:
            odd += 1
            gap -= 1
        odd += gap // 2
        return odd
