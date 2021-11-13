'''
Title     : 985. Sum of Even Numbers After Queries
Category  : Array
URL       : https://leetcode.com/problems/sum-of-even-numbers-after-queries/
Author    : arsho
Created   : 04 February 2019
'''


class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        total = sum([A[i] for i in range(len(A)) if A[i] % 2 == 0])
        ar = []
        for query in queries:
            val, index = query

            if A[index] % 2 == 0:
                total -= A[index]
                if val % 2 == 0:
                    total += A[index] + val
            else:
                if val % 2 == 1:
                    total += A[index] + val
            A[index] += val
            ar.append(total)
        return ar
