"""
Title     : 1089. Duplicate Zeros
Category  : Array
URL       : https://leetcode.com/problems/duplicate-zeros/
Author    : arsho
Created   : 23 August 2020
"""
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        arr_length = len(arr)
        i = 0
        while i < arr_length:
            if arr[i] == 0:
                for j in range(arr_length - 1, i, -1):
                    arr[j] = arr[j - 1]
                i = i + 2
            else:
                i = i + 1
