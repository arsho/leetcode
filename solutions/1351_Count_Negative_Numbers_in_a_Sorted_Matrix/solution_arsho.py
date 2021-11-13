"""
Title     : 1351. Count Negative Numbers in a Sorted Matrix
Category  : Array
URL       : https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
Author    : arsho
Created   : 12 August 2020
"""
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        total_negative_numbers = 0
        for ar in grid:
            for i in range(n):
                if ar[i] < 0:
                    total_negative_numbers += n - i
                    break
        return total_negative_numbers
