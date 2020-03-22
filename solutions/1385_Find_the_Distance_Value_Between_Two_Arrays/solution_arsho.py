"""
Title     : 1385. Find the Distance Value Between Two Arrays
Category  : Array
URL       : https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
Author    : arsho
Created   : 22 March 2020
"""
from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int],
                             d: int) -> int:
        count = 0
        for i in arr1:
            is_valid = True
            for j in arr2:
                if abs(i - j) <= d:
                    is_valid = False
                    break
            if is_valid:
                count += 1
        return count
