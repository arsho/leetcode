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


"""
# Alternative solution (in place operation)
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        for i, val in enumerate(A):
            if val % 2 == 1:
                for j in range(i+1, len(A)):
                    if A[j] % 2 == 0:
                        A[i], A[j] = A[j], A[i]
                        break
        return A
"""