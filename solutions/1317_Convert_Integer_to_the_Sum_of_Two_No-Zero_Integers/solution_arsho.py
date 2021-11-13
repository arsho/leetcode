"""
Title     : 1317. Convert Integer to the Sum of Two No-Zero Integers
Category  : Math
URL       : https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
Author    : arsho
Created   : 20 January 2020
"""
from typing import List


class Solution:
    def is_number_contains_zero(self, n):
        while n > 0:
            if n % 10 == 0:
                return True
            n = n // 10
        return False

    def getNoZeroIntegers(self, n: int) -> List[int]:
        first_number = n - 1
        while True:
            second_number = n - first_number
            if self.is_number_contains_zero(
                    first_number) == False and self.is_number_contains_zero(
                    second_number) == False:
                return [first_number, second_number]
            first_number -= 1