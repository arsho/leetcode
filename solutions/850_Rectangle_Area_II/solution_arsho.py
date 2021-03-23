"""
Title     : 850. Rectangle Area II
Category  : Line Sweep
URL       : https://leetcode.com/problems/rectangle-area-ii/
Author    : arsho
Created   : 23 March 2021
"""
from typing import List


class Solution:

    def get_width(self, xs):
        width = 0
        xs = sorted(xs)
        left, right = xs[0]
        for x1, x2 in xs:
            if x1 > right:
                width += right - left
                left = x1
            right = max(right, x2)
        width += right - left
        return width

    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        ys = set()
        for x1, y1, x2, y2 in rectangles:
            ys.add(y1)
            ys.add(y2)
        ys = sorted(list(ys))
        area = 0

        for i in range(len(ys) - 1):
            xs = []
            for x1, y1, x2, y2 in rectangles:
                if y1 <= ys[i] < y2:
                    xs.append([x1, x2])
            if xs:
                width = self.get_width(xs)
                area += width * (ys[i + 1] - ys[i])
        return area % (10 ** 9 + 7)