"""
Title     : 2485. Find the Pivot Integer
Category  : Math
URL       : https://leetcode.com/problems/find-the-pivot-integer/
Author    : arsho
Created   : 21 January 2023
"""


class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        total = (n * (n + 1)) // 2
        left_sum = 0
        right_sum = total
        for i in range(1, n + 1):
            left_sum += i
            right_sum = (total - left_sum) + i
            if left_sum == right_sum:
                return i
        return -1
