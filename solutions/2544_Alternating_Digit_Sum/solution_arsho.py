"""
Title     : 2544. Alternating Digit Sum
Category  : Adhoc
URL       : https://leetcode.com/problems/alternating-digit-sum/
Author    : arsho
Created   : 22 January 2023
"""
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = str(n)
        total = 0
        sign = 1
        for i in s:
            total += int(i) * sign
            sign = sign * -1
        return total