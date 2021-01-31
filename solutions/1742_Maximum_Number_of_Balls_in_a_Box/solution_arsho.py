"""
Title     : 1742. Maximum Number of Balls in a Box
Category  : Array
URL       : https://leetcode.com/problems/maximum-number-of-balls-in-a-box/
Author    : arsho
Created   : 31 January 2021
"""


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = {}
        for i in range(lowLimit, highLimit + 1):
            digit_sum = sum([int(c) for c in str(i)])
            boxes[digit_sum] = boxes.get(digit_sum, 0) + 1
        return sorted(boxes.values(), reverse=True)[0]
