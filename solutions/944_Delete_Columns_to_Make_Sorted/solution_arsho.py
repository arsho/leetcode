'''
Title     : 944. Delete Columns to Make Sorted
Category  : Greedy
URL       : https://leetcode.com/problems/delete-columns-to-make-sorted/
Author    : arsho
Created   : 07 January 2019
'''


class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        count = 0
        ar_length = len(A)
        str_length = len(A[0])
        for i in range(str_length):
            flag = True
            for j in range(1, ar_length):
                if A[j][i] < A[j - 1][i]:
                    flag = False
                    break
            if not flag:
                count += 1
        return count
