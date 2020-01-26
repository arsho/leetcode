"""
Title     : 1331. Rank Transform of an Array
Category  : Array
URL       : https://leetcode.com/problems/rank-transform-of-an-array/
Author    : arsho
Created   : 26 January 2020
"""
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_ar = sorted(arr)
        rank = 0
        prev = None
        d = {}
        for i in sorted_ar:
            if prev != None:
                if i != prev:
                    rank += 1
            else:
                rank += 1
            if i not in d:
                d[i] = rank
            prev = i
        result = []
        for i in arr:
            result.append(d[i])
        return result