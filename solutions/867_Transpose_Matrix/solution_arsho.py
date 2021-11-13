'''
Title     : 867. Transpose Matrix
Category  : Array
URL       : https://leetcode.com/problems/transpose-matrix/
Author    : arsho
Created   : 07 February 2019
'''


class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(A)
        m = len(A[0])
        ar = [[] for i in range(m)]
        for i in range(m):
            for j in range(n):
                ar[i].append(A[j][i])
        return ar
