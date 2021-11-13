'''
Title     : 509. Fibonacci Number
Category  : Array
URL       : https://leetcode.com/problems/fibonacci-number/
Author    : arsho
Created   : 12 January 2019
'''


class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1:
            return 1
        a = 0
        b = 1
        for i in range(2, N + 1):
            temp = a + b
            a, b = b, temp
        return b
