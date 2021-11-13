"""
Title     : 11. Container With Most Water
Category  : Two Pointers
URL       : https://leetcode.com/problems/container-with-most-water/
Author    : arsho
Created   : 24 July 2020
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        number_of_points = len(height)
        max_area = 0
        left = 0
        right = number_of_points - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(area, max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
