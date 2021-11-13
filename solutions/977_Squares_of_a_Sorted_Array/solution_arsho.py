'''
Title     : 977. Squares of a Sorted Array
Category  : Sort
URL       : https://leetcode.com/problems/squares-of-a-sorted-array/
Author    : arsho
Created   : 20 January 2019
'''


class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted([i ** 2 for i in A])
