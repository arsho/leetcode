"""
Title     : 1725. Number Of Rectangles That Can Form The Largest Square
Category  : Greedy
URL       : https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/
Author    : arsho
Created   : 21 January 2021
"""
from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        number_of_largest_squares = 0
        largest_square_side = 0
        for rectangle in rectangles:
            min_rectangle_side = min(rectangle)
            if min_rectangle_side > largest_square_side:
                number_of_largest_squares = 1
                largest_square_side = min_rectangle_side
            elif min_rectangle_side == largest_square_side:
                number_of_largest_squares += 1
        return number_of_largest_squares

if __name__ == "__main__":
    solution = Solution()

    rectangles = [[5, 8], [3, 9], [5, 12], [16, 5]]
    expected_output = 3
    result = solution.countGoodRectangles(rectangles)
    assert result == expected_output, "Error in {}, Expected {}, found {}"\
        .format(rectangles, expected_output, result)

    rectangles = [[2,3],[3,7],[4,3],[3,7]]
    expected_output = 3
    result = solution.countGoodRectangles(rectangles)
    assert result == expected_output, "Error in {}, Expected {}, found {}"\
        .format(rectangles, expected_output, result)