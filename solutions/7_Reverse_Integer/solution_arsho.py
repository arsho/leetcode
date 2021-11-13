"""
Title     : 7. Reverse Integer
Category  : Math
URL       : https://leetcode.com/problems/reverse-integer/
Author    : arsho
Created   : 06 September 2020
"""


class Solution:
    def reverse(self, x: int) -> int:
        min_range = (-2) ** 31
        max_range = (2 ** 31) - 1
        negative = False
        if x < 0:
            negative = True
            x = x * -1
        digits = []
        while x > 0:
            digits.append(x % 10)
            x = x // 10
        power = len(digits) - 1
        new_x = 0
        for i in digits:
            new_x = new_x + i * (10 ** power)
            power -= 1
            if new_x < min_range or new_x > max_range:
                return 0
        if negative:
            return new_x * -1
        return new_x


# Alternative Solution
"""
class Solution:
    def reverse(self, x: int) -> int:
        min_range = (-2) ** 31
        max_range = (2 ** 31) - 1
        negative = False
        if x < 0:
            negative = True
            x *= -1
        x = int(str(x)[::-1])
        if x < min_range or x > max_range:
            return 0
        if negative:
            return x * -1
        return x
"""
