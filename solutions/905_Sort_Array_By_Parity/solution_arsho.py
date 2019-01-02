'''
Title     : 905. Sort Array By Parity
Category  : Array
URL       : https://leetcode.com/problems/sort-array-by-parity/
Author    : arsho
Created   : 02 January 2019
'''


class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = []
        even = []
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        return even + odd
