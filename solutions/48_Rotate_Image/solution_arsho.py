"""
Title     : 48. Rotate Image
Category  : Array
URL       : https://leetcode.com/problems/rotate-image/
Author    : arsho
Created   : 05 September 2020
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix_length = len(matrix)
        for i in range(matrix_length // 2):
            for j in range(len(matrix[0])):
                matrix[i][j], matrix[matrix_length - i - 1][j] = \
                matrix[matrix_length - i - 1][j], matrix[i][j]
        for i in range(matrix_length):
            for j in range(matrix_length):
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


"""        
# Using extra memory 
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        new_matrix = [[0 for j in range(len(matrix[0]))] for i in
                      range(len(matrix))]
        row = 0
        for i in range(len(matrix)):
            col = 0
            for j in range(len(matrix[0]) - 1, -1, -1):
                val = matrix[j][i]
                new_matrix[row][col] = val
                col += 1
            row += 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0]) - 1, -1, -1):
                matrix[i][j] = new_matrix[i][j]
"""
