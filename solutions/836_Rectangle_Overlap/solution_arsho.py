"""
Title     : 836. Rectangle Overlap
Category  : Math
URL       : https://leetcode.com/problems/rectangle-overlap/
Author    : arsho
Created   : 23 March 2021
"""
from typing import List


class Solution:
    def isRectangleOverlap(self, rect1: List[int], rect2: List[int]) -> bool:
        x_distance = min(rect1[2], rect2[2]) - max(rect1[0], rect2[0])
        y_distance = min(rect1[3], rect2[3]) - max(rect1[1], rect2[1])
        return x_distance > 0 and y_distance > 0
