"""
Title     : 1624. Largest Substring Between Two Equal Characters
Category  : String
URL       : https://leetcode.com/problems/largest-substring-between-two-equal-characters/
Author    : arsho
Created   : 26 October 2020
"""


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max_distance = -1
        char_positions = {}
        for i,c in enumerate(s):
            if c in char_positions:
                char_positions[c].append(i)
                distance = i - char_positions[c][0] - 1
                max_distance = max(distance, max_distance)
            else:
                char_positions[c] = [i]
        return max_distance
