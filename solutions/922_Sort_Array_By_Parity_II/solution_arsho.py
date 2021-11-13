'''
Title     : 922. Sort Array By Parity II
Category  : Array
URL       : https://leetcode.com/problems/sort-array-by-parity-ii/
Author    : arsho
Created   : 17 June 2019
'''


class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = []
        even = []
        n = len(A)
        number_of_even_elements = n // 2
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        even = sorted(even)
        odd = sorted(odd)
        result = []
        for i in range(number_of_even_elements):
            result.append(even[i])
            result.append(odd[i])
        return result
