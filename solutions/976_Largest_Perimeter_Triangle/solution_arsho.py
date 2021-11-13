"""
Title     : 976. Largest Perimeter Triangle
Category  : Math
URL       : https://leetcode.com/problems/largest-perimeter-triangle/
Author    : arsho
Created   : 20 January 2020
"""
from typing import List


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A = sorted(A, reverse=True)
        for i in range(len(A) - 2):
            x = A[i]
            y = A[i + 1]
            z = A[i + 2]
            if (y + z) > x:
                return x + y + z
        return 0
