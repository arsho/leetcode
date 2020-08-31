"""
Title     : 350. Intersection of Two Arrays II
Category  : Hash Table
URL       : https://leetcode.com/problems/intersection-of-two-arrays-ii/
Author    : arsho
Created   : 01 September 2020
"""
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        occurrences = {}
        intersections = []
        for i in nums1:
            occurrences[i] = occurrences.get(i, 0) + 1
        for i in nums2:
            if occurrences.get(i, 0) > 0:
                intersections.append(i)
                occurrences[i] -= 1
        return intersections
