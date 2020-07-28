"""
Title     : 1528. Shuffle String
Category  : Sort
URL       : https://leetcode.com/problems/shuffle-string/
Author    : arsho
Created   : 28 July 2020
"""
from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = ["" for i in range(len(s))]
        position = 0
        for index in indices:
            result[index] = s[position]
            position += 1
        return "".join(result)
