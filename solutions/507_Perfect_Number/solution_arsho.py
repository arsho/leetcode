'''
Title     : 507. Perfect Number
Category  : Math
URL       : https://leetcode.com/problems/perfect-number/
Author    : arsho
Created   : 14 January 2019
'''
import math


class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        total = 0
        increment = 1
        if num % 2 == 1:
            increment = 2
        for i in range(1, math.ceil(num ** 0.5), increment):
            if num % i == 0:
                d = num // i
                total += i
                if d != num:
                    total += d
                if total > num:
                    return False
        return total == num
