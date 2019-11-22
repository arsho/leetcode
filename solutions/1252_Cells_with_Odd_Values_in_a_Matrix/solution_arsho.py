'''
Title     : 1252. Cells with Odd Values in a Matrix
Category  : Array
URL       : https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
Author    : arsho
Created   : 22 November 2019
'''


class Solution:
    def oddCells(self, n: int, m: int, indices) -> int:
        ar = [[0 for j in range(m)] for i in range(n)]
        for indice in indices:
            row, column = indice
            for i in range(m):
                ar[row][i] += 1
            for i in range(n):
                ar[i][column] += 1
        odd_count = 0
        for i in range(n):
            for j in range(m):
                if ar[i][j] % 2 == 1:
                    odd_count += 1
        return odd_count
