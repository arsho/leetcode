"""
Title     : 812. Largest Triangle Area
Category  : Math
URL       : https://leetcode.com/problems/largest-triangle-area/
Author    : arsho
Created   : 21 January 2020
"""
from itertools import combinations
from typing import List


class Solution:
    def get_triangle_area(self, points):
        area = points[0][0] * (points[1][1] - points[2][1]) + points[1][0] * (
                    points[2][1] - points[0][1]) + points[2][0] * (
                           points[0][1] - points[1][1])
        return abs(area) / 2

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        triplets = list(combinations(points, 3))
        max_area = 0
        for points in triplets:
            area = self.get_triangle_area(points)
            max_area = max(area, max_area)
        return max_area
