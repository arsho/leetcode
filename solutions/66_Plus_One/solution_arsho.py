"""
Title     : 66. Plus One
Category  : Array
URL       : https://leetcode.com/problems/plus-one/
Author    : arsho
Created   : 01 September 2020
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digit_sum = digits[i] + carry
            carry = digit_sum // 10
            digits[i] = digit_sum % 10
        if carry == 1:
            digits.insert(0, 1)
        return digits


# Alternative solution
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        current_number = "".join([str(i) for i in digits])
        new_number = int(current_number) + 1
        return [int(i) for i in str(new_number)]
"""
