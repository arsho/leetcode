"""
Title     : 1732. Find the Highest Altitude
Category  : Array
URL       : https://leetcode.com/problems/find-the-highest-altitude/
Author    : arsho
Created   : 03 February 2021
"""
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_gain = 0
        current_height = 0
        for i in gain:
            current_height += i
            highest_gain = max(current_height, highest_gain)
        return highest_gain
