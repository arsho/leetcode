"""
Title     : 223. Rectangle Area
Category  : Math
URL       : https://leetcode.com/problems/rectangle-area/
Author    : arsho
Created   : 23 March 2021
"""


class Solution:
    def get_rectangle_area(self, A: int, B: int, C: int, D: int) -> int:
        return abs(C - A) * abs(D - B)

    def get_rectangles_intersected_area(self, A: int, B: int, C: int, D: int,
                                        E: int, F: int, G: int, H: int) -> int:
        x_distance = min(C, G) - max(A, E)
        y_distance = min(D, H) - max(B, F)
        if x_distance > 0 and y_distance > 0:
            return x_distance * y_distance
        return 0

    def computeArea(self, A: int, B: int, C: int, D: int,
                    E: int, F: int, G: int, H: int) -> int:
        return self.get_rectangle_area(A, B, C, D) + \
               self.get_rectangle_area(E, F, G, H) - \
               self.get_rectangles_intersected_area(A, B, C, D, E, F, G, H)
