"""
Title     : 263. Ugly Number
Category  : Math
URL       : https://leetcode.com/problems/ugly-number/
Author    : arsho
Created   : 22 January 2020
"""
from math import ceil


class Solution:
    def is_prime(self, num: int) -> bool:
        if num == 1 or num % 2 == 0:
            return False
        for i in range(3, int(ceil(num ** 0.5)) + 1, 2):
            if num % i == 0:
                return False
        return True

    def isUgly(self, num: int) -> bool:
        if num == 1:
            return True
        if num <= 0:
            return False
        allowed_prime_factors = [2, 3, 5]
        if self.is_prime(num) and num not in allowed_prime_factors:
            return False
        for i in range(2, int(ceil(num ** 0.5)) + 1):
            if num % i == 0:
                res = num // i
                if self.is_prime(i) and i not in allowed_prime_factors:
                    return False
                if self.is_prime(res) and res not in allowed_prime_factors:
                    return False
        return True
