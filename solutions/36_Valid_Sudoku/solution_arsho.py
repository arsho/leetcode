"""
Title     : 36. Valid Sudoku
Category  : Hash Table
URL       : https://leetcode.com/problems/valid-sudoku/
Author    : arsho
Created   : 04 September 2020
"""
from typing import List


class Solution:
    def is_horizontal_valid(self, board: List[List[str]]):
        for i in range(len(board)):
            row_data = {}
            for j in range(len(board[0])):
                current_value = board[i][j]
                if current_value != ".":
                    if current_value in row_data:
                        return False
                    row_data[current_value] = True
        return True

    def is_vertical_valid(self, board: List[List[str]]):
        for i in range(len(board)):
            col_data = {}
            for j in range(len(board[0])):
                current_value = board[j][i]
                if current_value != ".":
                    if current_value in col_data:
                        return False
                    col_data[current_value] = True
        return True

    def is_boxes_valid(self, board: List[List[str]]):
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                box_data = {}
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        current_value = board[k][l]
                        if current_value != ".":
                            if current_value in box_data:
                                return False
                            box_data[current_value] = True
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.is_horizontal_valid(board) and self.is_vertical_valid(
            board) and self.is_boxes_valid(board)
